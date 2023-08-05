#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of the Wapiti project (https://wapiti-scanner.github.io)
# Copyright (C) 2019-2022 Nicolas Surribas
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
from typing import Optional
from urllib.parse import urlparse

from httpx import RequestError

from wapitiCore.main.log import log_red, log_verbose
from wapitiCore.attack.attack import Attack, Flags
from wapitiCore.language.vulnerability import Messages
from wapitiCore.definitions.redirect import NAME, WSTG_CODE
from wapitiCore.net import Request, Response
from wapitiCore.parsers.html_parser import Html


class ModuleRedirect(Attack):
    """Detect Open Redirect vulnerabilities."""
    # Won't work with PHP >= 4.4.2

    name = "redirect"
    MSG_VULN = "Open Redirect"
    do_get = True
    do_post = False
    payloads = [("https://openbugbounty.org/", Flags()), ("//openbugbounty.org/", Flags())]

    def __init__(self, crawler, persister, attack_options, stop_event, crawler_configuration):
        super().__init__(crawler, persister, attack_options, stop_event, crawler_configuration)
        self.mutator = self.get_mutator()

    async def attack(self, request: Request, response: Optional[Response] = None):
        page = request.path

        for mutated_request, parameter, __, __ in self.mutator.mutate(request):
            log_verbose(f"[¨] {mutated_request.url}")

            try:
                response = await self.crawler.async_send(mutated_request)
            except RequestError:
                self.network_errors += 1
                continue

            html = Html(response.content, mutated_request.url)
            all_redirections = {response.redirection_url} | html.all_redirections
            if any(urlparse(url).netloc.endswith("openbugbounty.org") for url in all_redirections):
                await self.add_vuln_low(
                    request_id=request.path_id,
                    category=NAME,
                    request=mutated_request,
                    parameter=parameter,
                    info=f"{self.MSG_VULN} via injection in the parameter {parameter}",
                    wstg=WSTG_CODE,
                    response=response
                )

                if parameter == "QUERY_STRING":
                    injection_msg = Messages.MSG_QS_INJECT
                else:
                    injection_msg = Messages.MSG_PARAM_INJECT

                log_red("---")
                log_red(
                    injection_msg,
                    self.MSG_VULN,
                    page,
                    parameter
                )
                log_red(Messages.MSG_EVIL_REQUEST)
                log_red(mutated_request.http_repr())
                log_red("---")
