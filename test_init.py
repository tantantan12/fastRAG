from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Indexer

if __name__=='__main__':
    with Run().context(RunConfig(nranks=1, experiment="msmarco")):

        config = ColBERTConfig(
            nbits=2,
            root="experiments", #/path/to/experiments
        )
        indexer = Indexer(checkpoint="/Users/49280549/Library/CloudStorage/Box-Box/xGenAI-Jane/colbertv2.0", config=config)
        indexer.index(name="msmarco.nbits=2", collection="/Users/49280549/Library/CloudStorage/Box-Box/xGenAI-Jane/collection.tsv")