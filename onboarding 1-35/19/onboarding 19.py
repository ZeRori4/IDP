# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 19</title>
	<version>1.0</version>
    <parameter>
        <type>channel</type>
        <id>CHANNEL_FULL_GUID</id>
        <name>Канал</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>COLOR</id>
        <name>color</name>
        <value>#1FC619</value>
    </parameter>

    <resources>
        <resource>figures.py</resource>
    </resources>
</parameters>
'''

resources = {
    "figures.py": """
        eNrtV22L4zYQ/h7Ifxh8LHG23hCbtrQBF3a3t1DIh7LNt1KMk8hec46VSsptcun9945ebMuO
        nd0sV0qPellHlmZGM/M8kkbv4Ob6BlZ0nRXpDHYiuflB9gwHw0G22VIm4IlyIT8FO8yGA8An
        YXQDTyTfEsbBSKVERDlNU8KGA7Jfka2AX9TIe8YosxWlFE5mKc6VHsS8YWU40C0IrW53LAei
        6CNOndEiinDUCSbBZOqU8pM1We5S17niYKRmcMUdD6KoiDckimSr0lf2hoM1SWDN4md39RQX
        BcmjdJetPbhOsnTHCB+bABzH+RmlwHQDLcAoSCNS4pal3AjLxzYHLhdsPGv0VWZ1oxmBniXi
        RLijKz7yMIwxxtF0sfRQG5BgTSy9pmyeceGWClbkq5zErCFrBXwvB6uIFYRfNGbbZUY29CNp
        elK7mWcFcfeHyPcA3wFmguaUhc47/+H+e/9HTM1zthZPYdCGSyp2uiqNgTvHtPyeFcIDfP2B
        3s5RHriIkZ5bin04EWW4QmJBeEM56FMmxVqr8m5d5blKjgd0K5CKcV7qqjEPMOJ4l4sZVPHV
        6ipOcNW0bXU1ZqkHJUyPROxYYYeP07fA2GNuDz4uKpkZ04WJPgS6K9BdTFkCR+YVjnt/NvGT
        z3A8lI19UPaUDRXTjGNLuTdbf3YmCWWbWLhWQv1Qzx8eJMRBqKcODxXUJjUaZvXW2hZJGFmJ
        cyRpc0PKX8QNkggQdPsGZjxm6ZOAJRUC19AZ9TeS459CWWboMpTfju0JnEmW55dCWur8D+s5
        WMss/WvQCrIXEf4jtJ768GCZRiW299/dv7//Fvf0hBai6p2qp+zl2ScSbfehf7Ljl7Z7KNCB
        4m9qu5d65zBU4+ZMW1T25VO6fgrwXbz6kDK6wyPhFGYTZm2nDvfU0gNVfikbthGTlZYRk53T
        Y0KZkaO2Ff+ycwIRVqxqcqpMOzKoJJD+neLfsUyROgfqOOtP4zGeDnCUpnr4Fu69+usQHrxT
        FMKy4XVlNqybXnfSQvvDa+IfKq520nlJ965mcpxnaRE6i7nkKq60cMF25MWdy9joZG0/9dRc
        4I4W89Ffo8Ujvu5k6+5x1IBdKhnZCvXF3Iof3QR3SWneZIvsVpMjJQsqLPr6L25uCx3Ql9nf
        bJZJo1Pzd1RBaRqhs4o+NbP6iaQxUm8Dkny1ao0K8RPAtzQ/uNe6ysOrwvWH5xgRa0MqpTrx
        NJodW9GvqKJKqzdUkNtS9+1VZGXipJKcTF/FFq5MQJaAJP0lCOugQtCpnOC9z3VUH66ietFo
        We19U1b1oWxgZGLOCe7qOSlcncsx/AR4SDmP5M9dxsgaAsnqDWVdyTZOmbuJOGxJazprRDoo
        o3bGZbxZ0tQMjQDEeBA0reQ5qj/EOSdjyLjK2szOtD2/EleGyonktQz7j5bc+YrbEgytdn+R
        bbKJ6nrjzwqTLctL6cU36EZ7669mldu23K3Htd9qOTPJantNqWveq9ZV773uP7q2XrdQvpal
        IvPgjL9GFi8xL4RFebwkOXd1ceyZWryvoK1L36ry5c/xVtUNbe5r+6Dtd5e4vuKeYhz+WuVS
        38A+6NPoG2hVqiiQvLY+bRTLqLi8qESWeSl9Um2dCJjO4BZu4M4DH6tubN02a5Uzyysr0p5i
        o4HlSdnaKGmlL6r4ePlC1VGNdJenHRWt5oV8eWfuXlW58jdM0WML
    """,
}
t1utils.resources_check(script_path, resources)

import figures

GLOBALS = globals()

COLOR = GLOBALS.get("COLOR", "")
CHANNEL_FULL_GUID = GLOBALS.get("CHANNEL_FULL_GUID", "")

channel_guid = CHANNEL_FULL_GUID.split("_")[0]

figures.draw(
    channel_guid,
    figures.rect([20, 40], [50, 60], color=COLOR),
)

