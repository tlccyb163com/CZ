# -*- coding: utf8 -*-

import os

#set del scw bl deb methods of parameters
def paramater(action,mo,canshu,value):
    if action.lower()=="set":
        content="set %s %s %s \n"%(mo,canshu,value)
    else:
        content="%s %s \n" % (action, mo)

    return  content


def crUtraNetwork():

    return "cr ENodeBFunction=1,UtraNetwork=1\n\n"

#crUtranFrequency
def crUtranFrequency(DLfrequency):
    content="cr ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s\n" \
            "%s\n\n"%(DLfrequency,DLfrequency)

    return content

#Create 3G cell frequency point
def crUtranFreqRelation(EUtranCellFDD,UtranFreqRelation,cellReselectionPriority,connectedModeMobilityPrio,csFallbackPrio,csFallbackPrioEC,mobilityActionCsfb):
    content="cr ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s\n" \
            "ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s\n" \
            "%s\n\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s cellReselectionPriority %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s connectedModeMobilityPrio %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s csFallbackPrio %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s csFallbackPrioEC %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s mobilityActionCsfb %s\n" \
            "\n"%(EUtranCellFDD,UtranFreqRelation,UtranFreqRelation,cellReselectionPriority,EUtranCellFDD,UtranFreqRelation,cellReselectionPriority,EUtranCellFDD,UtranFreqRelation,connectedModeMobilityPrio,EUtranCellFDD,UtranFreqRelation,csFallbackPrio,EUtranCellFDD,UtranFreqRelation,csFallbackPrioEC,EUtranCellFDD,UtranFreqRelation,mobilityActionCsfb)

    return content

#Create external definition 3G
def crExternalUtranCellFDD(DLfrequency,RNCid,cId,physicalCellIdentity,mcc,mnc,mncLength,rac,lac):
    content="cr ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s,ExternalUtranCellFDD=%s-%s\n" \
            "%s\n" \
            "rncId=%s,cId=%s\n" \
            "mcc=%s,mnc=%s,mncLength=%s\n" \
            "\n" \
            "set ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s,ExternalUtranCellFDD=%s-%s rac %s\n" \
            "set ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s,ExternalUtranCellFDD=%s-%s lac %s\n\n" \
            ""%(DLfrequency,RNCid,cId,physicalCellIdentity,RNCid,cId,mcc,mnc,mncLength,DLfrequency,RNCid,cId,rac,DLfrequency,RNCid,cId,lac)

    return content

#Create 4G -- > 3G neighborhood


def crUtranCellRelation(EUtranCellFDD,DLfrequency,cId,RNCid):
    content="cr ENodeBFunction=1,EUtranCellFDD=%s,UtranFreqRelation=%s,UtranCellRelation=%s\n" \
            "ENodeBFunction=1,UtraNetwork=1,UtranFrequency=%s,ExternalUtranCellFDD=%s-%s\n" \
            "\n"%(EUtranCellFDD,DLfrequency,cId,DLfrequency,RNCid,cId)
    return content

#CREUtranFrequency
def crEUtranFrequency(EUtranFreqRelation):
    content="cr ENodeBFunction=1,EUtraNetwork=1,EUtranFrequency=%s\n" \
            "%s\n\n"%(EUtranFreqRelation,EUtranFreqRelation)

    return content

#Create 4G frequency point

def crEUtranFreqRelation(EUtranCellFDD,EUtranFreqRelation,cellReselectionPriority,connectedModeMobilityPrio):
    content="cr ENodeBFunction=1,EUtranCellFDD=%s,EUtranFreqRelation=%s\n" \
            "ENodeBFunction=1,EUtraNetwork=1,EUtranFrequency=%s\n" \
            "%s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,EUtranFreqRelation=%s connectedModeMobilityPrio %s\n" \
            "\n"%(EUtranCellFDD,EUtranFreqRelation,EUtranFreqRelation,cellReselectionPriority,EUtranCellFDD,EUtranFreqRelation,connectedModeMobilityPrio)

    return content


def crExternalENodeBFunction(ExternalENodeBFunction,mcc,mnc,mncLength,ENodeBId):
    content="cr ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=%s\n" \
            "mcc=%s,mnc=%s,mncLength=%s\n" \
            "%s\n" \
            "\n"%(ExternalENodeBFunction,mcc,mnc,mncLength,ENodeBId)

    return content

def crTermPointToENB(ExternalENodeBFunction,ipAddress):
    content="cr ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=%s,TermPointToENB=%s\n" \
            "set ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=%s,TermPointToENB=%s ipAddress %s\n" \
            "\n"%(ExternalENodeBFunction,ExternalENodeBFunction,ExternalENodeBFunction,ExternalENodeBFunction,ipAddress)

    return content

def crExternalEUtranCellFDD(ExternalENodeBFunction,EUtranCellRelation,CellId,physicalLayerCellIdGroup,physicalLayerSubCellId,tac,EUtranFreqRelation):
    content="cr ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=%s,ExternalEUtranCellFDD=%s\n" \
            "%s\n" \
            "%s\n" \
            "%s\n" \
            "%s\n" \
            "ENodeBFunction=1,EUtraNetwork=1,EUtranFrequency=%s\n" \
            "\n"%(ExternalENodeBFunction,EUtranCellRelation,CellId,physicalLayerCellIdGroup,physicalLayerSubCellId,tac,EUtranFreqRelation)

    return content



def croutEUtranCellRelation(EUtranCellFDD,EUtranFreqRelation,EUtranCellRelation,ExternalENodeBFunction):
    content="cr ENodeBFunction=1,EUtranCellFDD=%s,EUtranFreqRelation=%s,EUtranCellRelation=%s\n" \
            "ENodeBFunction=1,EUtraNetwork=1,ExternalENodeBFunction=%s,ExternalEUtranCellFDD=%s\n" \
            "\n"%(EUtranCellFDD,EUtranFreqRelation,EUtranCellRelation,ExternalENodeBFunction,EUtranCellRelation)
    return content



def crinsideEUtranCellRelation(EUtranCellFDD,EUtranFreqRelation,EUtranCellRelation):
    content="cr ENodeBFunction=1,EUtranCellFDD=%s,EUtranFreqRelation=%s,EUtranCellRelation=%s-%s\n" \
            "EUtranCellFDD=%s\n" \
            "\n"%(EUtranCellFDD,EUtranFreqRelation,EUtranCellFDD,EUtranCellRelation,EUtranCellRelation)

    return content

def crGeraNetwork():
    return "cr ManagedElement=1,ENodeBFunction=1,GeraNetwork=1\n\n"


def crGeranFreqGroup(GeranFreqGroup):
    if GeranFreqGroup=="1800":
       GeranFreqGroupid="2"
    else:
       GeranFreqGroupid="1"
    content="cr ManagedElement=1,ENodeBFunction=1,GeraNetwork=1,GeranFreqGroup=%s\n" \
            "%s\n" \
            "\n"%(GeranFreqGroup,GeranFreqGroupid)

    return content

def crGeranFreqGroupRelation(EUtranCellFDD,GeranFreqGroup,cellReselectionPriority,connectedModeMobilityPrio,csFallbackPrio,csFallbackPrioEC,threshXLow,qRxLevMin,mobilityAction,mobilityActionCsfb):
    content="cr ManagedElement=1,ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s\n" \
            "ENodeBFunction=1,GeraNetwork=1,GeranFreqGroup=%s\n" \
            "%s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s connectedModeMobilityPrio %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s csFallbackPrio %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s csFallbackPrioEC %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s threshXLow %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s qRxLevMin %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s mobilityAction %s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s mobilityActionCsfb %s \n" \
            "\n"%(EUtranCellFDD,GeranFreqGroup,GeranFreqGroup,cellReselectionPriority,EUtranCellFDD,GeranFreqGroup,connectedModeMobilityPrio,EUtranCellFDD,GeranFreqGroup,csFallbackPrio,EUtranCellFDD,GeranFreqGroup,csFallbackPrioEC,EUtranCellFDD,GeranFreqGroup,threshXLow,EUtranCellFDD,GeranFreqGroup,qRxLevMin,EUtranCellFDD,GeranFreqGroup,mobilityAction,EUtranCellFDD,GeranFreqGroup,mobilityActionCsfb)
    return content


def crGeranFrequency(GeranFreqGroup,BCCH,):
    content="cr ManagedElement=1,ENodeBFunction=1,GeraNetwork=1,GeranFrequency=%s__%s\n" \
            "%s\n" \
            "0\n" \
            "set ENodeBFunction=1,GeraNetwork=1,GeranFrequency=%s__%s geranFreqGroupRef ENodeBFunction=1,GeraNetwork=1,GeranFreqGroup=%s\n" \
            "\n"%(GeranFreqGroup,BCCH,BCCH,GeranFreqGroup,BCCH,GeranFreqGroup)

    return content


def crExternalGeranCell(GeranFreqGroup,BCCH,mcc,mnc,mncLength,LAC,CI,BCC,NCC,GSMCELLNAME,rimCapable):
    content="cr ManagedElement=1,ENodeBFunction=1,GeraNetwork=1,ExternalGeranCell=%s__%s\n" \
            "mcc=%s,mnc=%s,mncLength=%s\n" \
            "%s\n" \
            "%s\n" \
            "%s\n" \
            "%s\n" \
            "ENodeBFunction=1,GeraNetwork=1,GeranFrequency=%s__%s\n" \
            "set ENodeBFunction=1,GeraNetwork=1,ExternalGeranCell=%s__%s rimCapable %s\n" \
            "set ENodeBFunction=1,GeraNetwork=1,ExternalGeranCell=%s__%s masterGeranCellId %s\n" \
            "\n"%(GeranFreqGroup,GSMCELLNAME,mcc,mnc,mncLength,LAC,CI,BCC,NCC,GeranFreqGroup,BCCH,GeranFreqGroup,GSMCELLNAME,rimCapable,GeranFreqGroup,GSMCELLNAME,GSMCELLNAME)

    return content


def crGeranCellRelation(EUtranCellFDD,GeranFreqGroup,GSMCELLNAME,coverageIndicator):
    content="cr ManagedElement=1,ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s,GeranCellRelation=%s\n" \
            "ENodeBFunction=1,GeraNetwork=1,ExternalGeranCell=%s__%s\n" \
            "set ENodeBFunction=1,EUtranCellFDD=%s,GeranFreqGroupRelation=%s,GeranCellRelation=%s coverageIndicator %s\n" \
            "\n"%(EUtranCellFDD,GeranFreqGroup,GSMCELLNAME,GeranFreqGroup,GSMCELLNAME,EUtranCellFDD,GeranFreqGroup,GSMCELLNAME,coverageIndicator)

    return content


def crMeasBasedCsfb(EUtranCellFDD,GeranFreqGroup,thresholdRscp,altCsfbTargetPrio):
    content="set Licensing=1,OptionalFeatureLicense=MeasBasedCsfbTargetSelection featureState 1\n" \
            "set Lm=1,FeatureState=CXC4011664 featureState 1\n" \
            "set EUtranCellFDD=%s,UeMeasControl=1,ReportConfigCsfbUtra=1 thresholdRscp %s\n" \
            "set EUtranCellFDD=%s,GeranFreqGroupRelation=%s altCsfbTargetPrio %s\n" \
            "\n"%(EUtranCellFDD,thresholdRscp,EUtranCellFDD,GeranFreqGroup,altCsfbTargetPrio)

    return content


def crMeasBasedCsfbTargetSelection(EutranCellFDD,thresholdRscp,GeranFreqGroupRelation,altCsfbTargetPrio):
    content="set Licensing=1,OptionalFeatureLicense=MeasBasedCsfbTargetSelection featureState 1\n" \
            "set Lm=1,FeatureState=CXC4011664 featureState 1\n" \
            "set EUtranCellFDD=%s,UeMeasControl=1,ReportConfigCsfbUtra=1 thresholdRscp %s\n" \
            "set EUtranCellFDD=%s,GeranFreqGroupRelation=%s altCsfbTargetPrio %s\n" \
            "\n"%(EutranCellFDD,thresholdRscp,EutranCellFDD,GeranFreqGroupRelation,altCsfbTargetPrio)

    return content



