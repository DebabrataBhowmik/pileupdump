import FWCore.ParameterSet.Config as cms

process = cms.Process("pileupdump")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load("Configuration.Geometry.GeometryIdeal_cff" )
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '94X_dataRun2_ReReco_EOY17_v2')
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v12')
process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
        #'/store/mc/RunIIFall17MiniAOD/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/50000/0024A35F-86EB-E711-A5BC-A4BF0112BC06.root'
        #'/store/mc/RunIIFall17MiniAOD/GluGluHToGG_M70_13TeV_amcatnloFXFX_pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/70000/D09A8D92-09FA-E711-BF65-FA163EEFA3D2.root'
    )
)

process.pileupdump = cms.EDAnalyzer('pileupdump',
                            #OutputFileName = cms.string("PileUp.root"),
                            #    PileupSummaryInfoSrc = cms.InputTag("addPileupInfo")
                                    genParticleSrc       = cms.InputTag("prunedGenParticles"),
                                    generatorLabel = cms.InputTag("generator"),
                                    pileupCollection = cms.InputTag("slimmedAddPileupInfo"),  
                                    )

process.TFileService = cms.Service("TFileService",
  fileName = cms.string('pileup_withgenweight.root')
)

#process.Tracer = cms.Service("Tracer")
process.p = cms.Path(process.pileupdump)
