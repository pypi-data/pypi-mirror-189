# Copyright 2018-2023 contributors to the Marquez project
# SPDX-License-Identifier: Apache-2.0

class MarquezError(Exception):
    pass


class APIError(MarquezError):
    pass


class InvalidRequestError(MarquezError):
    pass
