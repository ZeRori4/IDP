# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 28</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>Имя шаблона</name>
        <id>NAME_TMPL</id>
        <value></value>
    </parameter>
    <resources>
        <resource>templates.py</resource>
    </resources>
</parameters>
'''

resources = {
    "templates.py": """
        eNrtV1tv2zYUfg+Q/8ARCCYNrpBgGAYE89Cic4oARTAkGfZQFIQi07YKSTRIOm1Q9L/3HF4k
        kpJdZ+vepjzEIg/P5eN3LqrbrZCabITSpyenJ1o+XZ6eEHhWUrRkw5stl4rUVmrNNWvEes3l
        6Qn/VPGtJtdmZyGlkOFBlKq7dXDwrTlHShVpOT2xv8g8WM5y3GDsEUzXomMMdulFcV5cUC9f
        LPnDbp3RM0Wc1CU5U3RGGOvKljOGv/rzRp/iEhbYelcvQR8GXCiuNXipMkrzAjdQDv77ffHw
        gVc6owJAKLWQsMXACjkjgbI8RM15V3crkVHUBA42olzyJVG7quIKfYT1Ar3MexQX3WMtRdfy
        LoLSunIjOh5p/1jKDty2BqyPpBOarMSuW1ITrObttik1V8zHOI65l8Ej/Usa+5m6HweMf1VT
        KkXu3TnjdrYw4QDmuYtgCzKh+GvJQTg+FL3tO+iFboS+wjCPO/Xmr2svl9mAvOSSr4AhdVdr
        xjLFm9WMeGS8CD71ql8u9NOWkx+Ail4lDQTxkWWtOLkHMRsYXXzagkm4e3+iVwYkgAvzXAoM
        5INK9KoIrs//TCQgrogk/QZjyDzmLtLc2hC55FvpIg/jlVzvZEfobyFyPWU+q2Jb6s2XPP+d
        Fish21Jnah75mZgJPbAoa1lzNf85NBqEEVIv0ls45vkzQ8r5J0q9tzbnPKt9lpgS4c35HPQK
        DufiNzF3dDHxJWcmcncsgE9PrVFaY3kj2RmQMwiiBwcjSdcQMAf32Fg+XjLQ67rlYqezX87P
        Z6Qp24dleTnFJqP2xUWe6OGN4vtj5yYr/nHkR0c9Ga5dfGnqQsv1RiwHnlamKjHPlqxqIEGt
        9kp0Gpgwhw4RBEYptZWMdPxjzzJvBJ9Xcp2yABWSTGmoVkNBwMVYzFkcSYKj5a7Rfj80dmuy
        NrUXpHCgxsIbncaylR6eKNSXSO+q7H6Ei6m7ILnKlYYObkCEO4hQChLWN5giRTsC+mCK9xbn
        BK6oQC96NezhybT+bDqr0/4xWbqnuhO9KusGS4lwNBm8+Pylr4LGaD6qoykzpuk3HUdPwoR4
        VxH2Zpx5eHI8OpJ/ZETA/5RLI+z3EGkPcwDivveRegB1mG2KRmX55agUx517HnZuUoLdqJDg
        Pv6fKF/uMuFCslGbG8gzmlAcEd3NbyVOkfppuHa8un0NeKqo7VVk6HKUovCyX+KL2cJBfKRr
        Rh7LZheRzyzgIKJlZjeHvXgsv+PaVEYDqG1Y6YHIsXcUJel7UG7kDgTr6sRR8b6jTpq+HzLQ
        rowCD/V+l9idwuPC7/08AgG1KSUfM8cQ3s4maXELoMG5R2ksu9TqobnJjDvzglXudSN2SxqO
        cdWm7Dpo7SzG6Ce/PprlfAsDvUDdX7M/Fn+/uv2T3S3u769v3tzNZrMXFzPs6DD90hktPoi6
        S+YCxLna5Cb5qw2mvbc2yEWzptqIj86xVsBYL+T8IoEHfJmeGf3NgYqhsg5jVtJR8MFPuN6i
        G7Wc2bD3jMeh9BMOCms48dhvRRpFtuQN1/wZ9x1Nwre8FY9B04JJiibB9MSwlobO7L70hhEp
        2zcUHR6IkmZ0xCD0zCFo3LSOaVijZvVvh56+bbmMC5w4PPXMh+nHA77mbqoYEI47f9L092K8
        r9l/J8ye19wPIXRwnAtgYUKy/+n4HDrGk7SDvieY3fn2nOzHoCnoB/5+BcXB6qY=
    """,
}
t1utils.resources_check(script_path, resources)

import host
import templates


def loop():
    all_channels = [guid for _, guid, _, _ in host.objects_list("Channel")]
    tmpl = templates.get_or_create(NAME_TMPL)
    tmpl.channels_content(*all_channels[:])
    host.timeout(1 * 1e3, loop)


loop()
