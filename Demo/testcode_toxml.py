from __future__ import annotations
import xml.etree.ElementTree as ETree
import re
from Code.xmlexporter import XMLModelConverter
from xml.dom.minidom import parseString
from Pydantic_Model.pydantic import (
    InterfaceContainer,
    NativeContainer,
    VlansContainer,
    Model,
    SwitchportConfigContainer,
    InterfaceListEntry,
    VlanContainer,
    AccessContainer,
    AccessLeaf,
    ModeContainer,
    SwitchportContainer,
    VlanContainer2,
    AllowedContainer,
    TrunkContainer,
    TrunkLeaf,
    ConfigContainer,
    VlanListEntry2,
)

""" This Public Module provides:
- Get Information from the GraphQL
- Load Data into Pydantic the Pydantic Model, generated from the openconfig Yang Files
- Generate an Netconf Conform XML with the XMLExporter class.
"""

def createModel():
    ETree.register_namespace("nc", "urn:ietf:params:xml:ns:netconf:base:1.0")
    
    model = Model(
        vlans=VlansContainer(
            vlan=[VlanListEntry2(
                vlan_id=3,
                config=ConfigContainer(
                    vlan_id=3,
                    name="Vlan3 - Management",
                ),
            ),
            VlanListEntry2(
                vlan_id=40,
                config=ConfigContainer(
                    vlan_id=40,
                    name="Vlan40 - Production",
                ),
            ),
            VlanListEntry2(
                vlan_id=500,
                config=ConfigContainer(
                    vlan_id=500,
                    name="Vlan500 - Testing",
                ),
            ),
            ],
        ),
        native=NativeContainer(
            interface=InterfaceContainer(
                gigabit_ethernet=[
                    InterfaceListEntry(
                        name="1/0/1",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(access=AccessLeaf()),
                                access=AccessContainer(
                                    vlan=VlanContainer(
                                        vlan=3
                                    )
                                ),
                            )
                        ),
                    ),
                    InterfaceListEntry(
                        name="1/0/2",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(access=AccessLeaf()),
                                access=AccessContainer(
                                    vlan=VlanContainer(
                                        vlan=4
                                    )
                                ),
                            )
                        ),
                    )
                ],
                ten_gigabit_ethernet=[
                    InterfaceListEntry(
                        name="1/0/11",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4,5"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                    InterfaceListEntry(
                        name="1/0/12",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                ],
                twenty_five_gig_e=[
                    InterfaceListEntry(
                        name="1/0/23",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4,5"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                    InterfaceListEntry(
                        name="1/0/24",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                ],
                forty_gigabit_ethernet=[
                    InterfaceListEntry(
                        name="1/0/31",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4,5"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                    InterfaceListEntry(
                        name="1/0/32",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(trunk=TrunkLeaf()),
                                trunk=TrunkContainer(
                                    allowed=AllowedContainer(
                                        vlan=VlanContainer2(
                                            vlans="3,4"
                                        )
                                    )
                                ),
                            )
                        ),
                    ),
                ],
            )
        )
    )
               
    xmlcontent = XMLModelConverter.to_xml(model)
    xml_string = ETree.tostring(xmlcontent, encoding="unicode")
    print(parseString(xml_string).toprettyxml())
    return parseString(xml_string).toprettyxml()

if __name__ == "__main__":
    createModel()