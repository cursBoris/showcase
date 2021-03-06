# coding: utf-8
'''
Created on 02.11.2011

@author: den
'''
from ru.curs.showcase.core.jython import JythonProc

# init vars
main = None
add = None
session = None
filterContext = None
elementId = None


class TestGoodSmall(JythonProc):
    def getRawData(self, context, element):
        global main, add, session, filterContext, elementId
        main = context.getMain()
        if context.getAdditional():
            add = context.getAdditional()
        session = context.getSession()
        if context.getFilter():
            filterContext = context.getFilter()
        elementId = element
        return mainproc()


def mainproc():
    return u'''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
    elementFormDefault="qualified">
    <xs:element name="documentset">
        <xs:complexType>
            <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="document"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="document">
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="0" ref="documentset"/>
                <xs:element minOccurs="0"  ref="Schema" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Schema">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="Temp" />
                <xs:element ref="Stat" />
                <xs:element ref="Info" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Temp">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="Flag" />
                <xs:element ref="Error" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Flag" type="xs:string" />
    <xs:element name="Error">
        <xs:complexType />
    </xs:element>
    <xs:element name="Stat">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="Isp" />
                <xs:element ref="DateIsp" />
                <xs:element ref="Uch" />
                <xs:element ref="DateUch" />
                <xs:element ref="AC" />
                <xs:element ref="DateAC" />
                <xs:element ref="Paper" />
                <xs:element ref="DatePaper" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Isp">
        <xs:complexType />
    </xs:element>
    <xs:element name="DateIsp">
        <xs:complexType />
    </xs:element>
    <xs:element name="Uch">
        <xs:complexType />
    </xs:element>
    <xs:element name="DateUch">
        <xs:complexType />
    </xs:element>
    <xs:element name="AC">
        <xs:complexType />
    </xs:element>
    <xs:element name="DateAC">
        <xs:complexType />
    </xs:element>
    <xs:element name="Paper">
        <xs:complexType />
    </xs:element>
    <xs:element name="DatePaper">
        <xs:complexType />
    </xs:element>
    <xs:element name="Info">
        <xs:complexType>
            <xs:choice maxOccurs="unbounded">
                <xs:element ref="Objective" />
                <xs:element ref="PriorDir" />
                <xs:element ref="Task" />
                <xs:element ref="ActionSuperviser" />
                <xs:element ref="ChangeStr" />
                <xs:element ref="Date" />
                <xs:element ref="Executor" />
                <xs:element ref="FIO" />
                <xs:element ref="FIOisp" />
                <xs:element ref="FIOuch" />
                <xs:element ref="History" />
                <xs:element ref="Nazn" />
                <xs:element ref="Num_table" />
                <xs:element ref="Period" />
                <xs:element ref="ProjectName" />
                <xs:element ref="ProjectNumber" />
                <xs:element ref="Responsible" />
                <xs:element ref="UserName" />
                <xs:element ref="Userisp" />
                <xs:element ref="Usertype" />
                <xs:element ref="datecheck" />
                <xs:element ref="datefill" />
                <xs:element ref="inyearperiod" />
                <xs:element ref="remark" />
                <xs:element ref="repcampaign" />
                <xs:element ref="roleacmanager" />
                <xs:element ref="roleoimanager" />
                <xs:element ref="status" />
                <xs:element ref="transition" />
                <xs:element ref="year" />
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="ActionSuperviser" type="xs:string" />
    <xs:element name="ChangeStr" type="xs:boolean" />
    <xs:element name="Date">
        <xs:complexType />
    </xs:element>
    <xs:element name="Executor">
        <xs:complexType />
    </xs:element>
    <xs:element name="FIO">
        <xs:complexType />
    </xs:element>
    <xs:element name="FIOisp">
        <xs:complexType />
    </xs:element>
    <xs:element name="FIOuch">
        <xs:complexType />
    </xs:element>
    <xs:element name="History">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="Rec" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Rec">
        <xs:complexType />
    </xs:element>
    <xs:element name="Nazn" type="xs:string" />
    <xs:element name="Num_table" type="xs:decimal" />
    <xs:element name="Period" type="xs:string" />
    <xs:element name="ProjectName" type="xs:string" />
    <xs:element name="ProjectNumber" type="xs:integer" />
    <xs:element name="Responsible" type="xs:string" />
    <xs:element name="UserName" type="xs:string" />
    <xs:element name="Userisp">
        <xs:complexType />
    </xs:element>
    <xs:element name="Usertype" type="xs:string" />
    <xs:element name="datecheck" type="xs:string" />
    <xs:element name="datefill" type="xs:string" />
    <xs:element name="inyearperiod" type="xs:NCName" />
    <xs:element name="remark">
        <xs:complexType />
    </xs:element>
    <xs:element name="repcampaign" type="xs:string" />
    <xs:element name="roleacmanager" type="xs:string" />
    <xs:element name="roleoimanager" type="xs:string" />
    <xs:element name="status" type="xs:string" />
    <xs:element name="transition" type="xs:string" />
    <xs:element name="year" type="xs:integer" />
    <xs:element name="PriorDir" type="xs:string" />

    <xs:element name="Task">
        <xs:complexType mixed="true">
            <xs:choice minOccurs="0" maxOccurs="unbounded">
                <xs:element ref="Action" />
                <xs:element ref="Indicator" />
            </xs:choice>
            <xs:attribute name="Code" type="xs:integer" />
            <xs:attribute name="Consider" />
            <xs:attribute name="GUID" />
            <xs:attribute name="Name" />
            <xs:attribute name="Napr" type="xs:NCName" />
            <xs:attribute name="resp" />
        </xs:complexType>
    </xs:element>
    <xs:element name="Objective">
        <xs:complexType mixed="true">
            <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="Indicator"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="Action">
        <xs:complexType>
            <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="Keypoint"/>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="Fin"/>
            </xs:sequence>
            <xs:attribute name="AntiKr" />
            <xs:attribute name="Cause1" />
            <xs:attribute name="Cause2" />
            <xs:attribute name="Code" use="required" />
            <xs:attribute name="Consider" use="required" type="xs:boolean" />
            <xs:attribute name="GUID" type="xs:integer" />
            <xs:attribute name="Name" use="required" />
            <xs:attribute name="Number" use="required" type="xs:integer" />
            <xs:attribute name="Pok1" use="required" />
            <xs:attribute name="Pok10" use="required" />
            <xs:attribute name="Pok11" use="required" />
            <xs:attribute name="Pok12" use="required" />
            <xs:attribute name="Pok13" use="required" />
            <xs:attribute name="Pok14" use="required" />
            <xs:attribute name="Pok15" use="required" />
            <xs:attribute name="Pok2" use="required" />
            <xs:attribute name="Pok3" use="required" />
            <xs:attribute name="Pok4" use="required" />
            <xs:attribute name="Pok5" use="required" />
            <xs:attribute name="Pok6" use="required" />
            <xs:attribute name="Pok7" use="required" />
            <xs:attribute name="Pok8" use="required" />
            <xs:attribute name="Pok9" use="required" />
            <xs:attribute name="resp" use="required" />
        </xs:complexType>
    </xs:element>
    <xs:element name="Keypoint">
        <xs:complexType>
            <xs:attribute name="Cause1" />
            <xs:attribute name="Cause2" />
            <xs:attribute name="Code" use="required" />
            <xs:attribute name="Consider" />
            <xs:attribute name="Name" use="required" />
            <xs:attribute name="Number" use="required" type="xs:integer" />
            <xs:attribute name="Pok1" use="required" />
            <xs:attribute name="Pok2" use="required" />
            <xs:attribute name="Pok3" use="required" />
            <xs:attribute name="Pok4" use="required" />
            <xs:attribute name="Pok5" use="required" />
            <xs:attribute name="Pok6" use="required" />
            <xs:attribute name="Pok7" use="required" />
        </xs:complexType>
    </xs:element>
    <xs:element name="Fin">
        <xs:complexType>
            <xs:attribute name="KBK" type="xs:integer" />
            <xs:attribute name="KBK_GRBS" type="xs:integer" />
            <xs:attribute name="KBK_podrazdel" />
            <xs:attribute name="KBK_rashod" />
            <xs:attribute name="KBK_razdel" />
            <xs:attribute name="KBK_statya" />
            <xs:attribute name="Number" use="required" />
            <xs:attribute name="Pok1" use="required" />
            <xs:attribute name="Pok2" use="required" />
            <xs:attribute name="Pok3" use="required" />
            <xs:attribute name="Pok4" use="required" />
            <xs:attribute name="Pok5" />
            <xs:attribute name="Pok6" />
            <xs:attribute name="Pok7" />
            <xs:attribute name="Rem" />
            <xs:attribute name="Rem1" />
            <xs:attribute name="Rem2" />
        </xs:complexType>
    </xs:element>
    <xs:element name="Indicator">
        <xs:complexType>
            <xs:attribute name="Code" use="required" />
            <xs:attribute name="Consider" type="xs:boolean" />
            <xs:attribute name="GUID" type="xs:decimal" />
            <xs:attribute name="Name" use="required" />
            <xs:attribute name="Number" use="required" type="xs:integer" />
            <xs:attribute name="Pok8" use="required" />
            <xs:attribute name="Pok9" use="required" />
            <xs:attribute name="Rem" use="required" />
        </xs:complexType>
    </xs:element>
</xs:schema>
    '''

if __name__ == "__main__":
    mainproc()
