from __future__ import annotations
import xml.etree.ElementTree as ETree
import re
from .Modules.xmlexporter import XMLModelConverter
from xml.dom.minidom import parseString
from .PydanticStructure.out import (
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
                        name="GigabitEthernet1/0/1",
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
                        name="GigabitEthernet1/0/2",
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
                        name="TenGigabitEthernet1/0/5",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(access=TrunkLeaf()),
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
                        name="TenGigabitEthernet1/0/7",
                        switchport_config=SwitchportConfigContainer(
                            switchport=SwitchportContainer(
                                mode=ModeContainer(access=TrunkLeaf()),
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
                ]
            )
        )
    )
               
    xmlcontent = XMLModelConverter.to_xml(model)
    xml_string = ETree.tostring(xmlcontent, encoding="unicode")
    print(parseString(xml_string).toprettyxml())
    return parseString(xml_string).toprettyxml()
