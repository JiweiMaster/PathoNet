class Config:
    def __init__(self):
        self.imageShape=(1024,1024,3)
        self.inputShape=(256,256,3)
        self.pretrainedModel=None
        self.classes=3
        self.model="PathoNet" #PathoNet,FRRN_A,FCRN_B,Deeplab_xception,Deeplab_mobilenet
        self.logPath="logs/"
        self.checkpointsPath="checkpoints/"
        self.data_path=""
        self.loss=""
        self.optimizer="adam"
        self.lr=1e-3
        self.batchSize=16
        self.epoches=30
        self.GaussianSize=9
        self.trainDataPath=""    