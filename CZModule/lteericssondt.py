# -*- coding: utf8 -*-

import os

#set del scw bl deb methods of parameters
def paramater(action,mo,canshu="",value=""):

    if action.lower()=="bl" or action.lower()=="deb":
       content="%s %s \n" % (action, mo)
    else:
        content="%s %s %s %s \n"%(action,mo,canshu,value)

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
    
    
    
def changeFrequency(ERBS,action,ExternalUtranCellFDD,parameter,UtranFrequency):
    content="acc %s %s\n"\
            "%s\n\n"%(ExternalUtranCellFDD,parameter,UtranFrequency)
    
    return content
    
    
    
def crutranrelation(SourceRNC,SourceCell,TargetRNC,TargetCell,hcsPrio,qHcs,penaltyTime,temporaryOffset1,temporaryOffset2,loadSharingCandidate,qOffset1sn,qOffset2sn,selectionPriority):
    if SourceRNC==TargetRNC:
       content='CREATE\n' \
               '(\n' \
               '   parent "ManagedElement=1,RncFunction=1,UtranCell=%s"\n' \
               '   identity "%s_%s"\n' \
               '   moType UtranRelation\n' \
               '   exception none\n' \
               '   nrOfAttributes 6\n' \
               '   utranCellRef Ref "ManagedElement=1,RncFunction=1,UtranCell=%s"\n' \
               '   hcsSib11Config Struct\n' \
               '   nrOfElements 5\n' \
               '    hcsPrio Integer %s\n' \
               '    qHcs Integer %s\n' \
               '    penaltyTime Integer %s\n' \
               '    temporaryOffset1 Integer %s\n' \
               '    temporaryOffset2 Integer %s\n' \
               '   selectionPriority Integer %s\n' \
               '   loadSharingCandidate Integer %s\n' \
               '   qOffset1sn Integer %s\n' \
               '   qOffset2sn Integer %s\n' \
               ')\n\n'%(SourceCell,SourceCell,TargetCell,TargetCell,hcsPrio,qHcs,penaltyTime,temporaryOffset1,temporaryOffset2,selectionPriority,loadSharingCandidate,qOffset1sn,qOffset2sn)
               
    else:
       content='CREATE\n' \
               '(\n' \
               '   parent "ManagedElement=1,RncFunction=1,UtranCell=%s"\n' \
               '   identity "%s_%s"\n' \
               '   moType UtranRelation\n' \
               '   exception none\n' \
               '   nrOfAttributes 6\n' \
               '   utranCellRef Ref "ManagedElement=1,RncFunction=1,IurLink=IurLink_%s,ExternalUtranCell=%s"\n' \
               '   hcsSib11Config Struct\n' \
               '   nrOfElements 5\n' \
               '    hcsPrio Integer %s\n' \
               '    qHcs Integer %s\n' \
               '    penaltyTime Integer %s\n' \
               '    temporaryOffset1 Integer %s\n' \
               '    temporaryOffset2 Integer %s\n' \
               '   selectionPriority Integer %s\n' \
               '   loadSharingCandidate Integer %s\n' \
               '   qOffset1sn Integer %s\n' \
               '   qOffset2sn Integer %s\n' \
               ')\n\n'%(SourceCell,SourceCell,TargetCell,TargetRNC,TargetCell,hcsPrio,qHcs,penaltyTime,temporaryOffset1,temporaryOffset2,selectionPriority,loadSharingCandidate,qOffset1sn,qOffset2sn)
    
    return content
    
    
def crgsmneighbor(SourceRNC,SourceCell,TargetGsmNetwork,TargetCell,mobilityRelationType,qOffset1sn,selectionPriority):
    content='CREATE\n' \
            '(\n' \
            '   parent "ManagedElement=1,RncFunction=1,UtranCell=%s"\n' \
            '   identity "%s_%s"\n' \
            '   moType GsmRelation\n' \
            '   exception none\n' \
            '   nrOfAttributes 4\n' \
            '   externalGsmCellRef Ref "ManagedElement=1,RncFunction=1,ExternalGsmNetwork=46001,ExternalGsmCell=%s"\n' \
            '   mobilityRelationType Integer %s\n' \
            '   qOffset1sn Integer %s\n' \
            '   selectionPriority Integer %s\n' \
            ')\n\n'%(SourceCell,SourceCell,TargetCell,TargetCell,mobilityRelationType,qOffset1sn,selectionPriority)
    
    return content

def crexternalutrancell(**kwargs):
    content='CREATE\n' \
            '(\n' \
            '   parent "ManagedElement=1,RncFunction=1,IurLink=IurLink_%s"\n' \
            '   identity "%s"\n' \
            '   moType ExternalUtranCell\n' \
            '   exception none\n' \
            '   nrOfAttributes 13\n' \
            '   cId Integer %s\n' \
            '   lac Integer %s\n' \
            '   rac Integer %s\n' \
            '   primaryScramblingCode Integer %s\n' \
            '   uarfcnDl Integer %s\n' \
            '   uarfcnUl Integer %s\n' \
            '   agpsEnabled Integer %s\n' \
            '   individualOffset Integer %s\n' \
            '   cellCapability Struct\n' \
            '   nrOfElements 4\n' \
            '      hsdschSupport Integer %s\n' \
            '      edchSupport Integer %s\n' \
            '      edchTti2Support Integer %s\n' \
            '      enhancedL2Support Integer %s\n' \
            '   maxTxPowerUl Integer %s\n' \
            '   qRxLevMin Integer %s\n' \
            '   qQualMin Integer %s\n' \
            '   userLabel String "%s"\n' \
            ')\n\n'%(kwargs.get("IurLinkID"),kwargs.get("ExternalCell"),kwargs.get("CID"),kwargs.get("LAC"),kwargs.get("RAC"),kwargs.get("PSC"),kwargs.get("uarfcnDl"),kwargs.get("uarfcnUl"),kwargs.get("agpsEnabled"),kwargs.get("individualOffset"),kwargs.get("hsdschSupport"),kwargs.get("edchSupport"),kwargs.get("edchTti2Support"),kwargs.get("enhancedL2Support"),kwargs.get("maxTxPowerUl"),kwargs.get("qRxLevMin"),kwargs.get("qQualMin"),kwargs.get("ExternalCell"))
    return content



def crexternalgsmcell(**kwargs):
    content='CREATE\n' \
            '(\n' \
            '   parent "ManagedElement=1,RncFunction=1,ExternalGsmNetwork=%s"\n' \
            '   identity "%s"\n' \
            '   moType ExternalGsmCell\n' \
            '   exception none\n' \
            '   nrOfAttributes 10\n' \
            '   cellIdentity Integer %s\n' \
            '   ncc Integer %s\n' \
            '   bcc Integer %s\n' \
            '   bcchFrequency Integer %s\n' \
            '   lac Integer %s\n' \
            '   bandIndicator Integer %s\n' \
            '   maxTxPowerUl Integer %s\n' \
            '   individualOffset Integer %s\n' \
            '   qRxLevMin Integer %s\n' \
            '   userLabel String "%s"\n' \
            ')\n\n'%(kwargs.get("ExternalGsmNetwork"),kwargs.get("ExternalGsmCell"),kwargs.get("cellIdentity"),kwargs.get("ncc"),kwargs.get("bcc"),kwargs.get("bcchFrequency"),kwargs.get("lac"),kwargs.get("bandIndicator"),kwargs.get("maxTxPowerUl"),kwargs.get("individualOffset"),kwargs.get("qRxLevMin"),kwargs.get("ExternalGsmCell"))
    return content
