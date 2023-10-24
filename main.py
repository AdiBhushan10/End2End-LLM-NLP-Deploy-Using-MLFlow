import transformers
import langchain
#from langchain import PromptTemplate, HuggingFaceHub, LLMchain
from langchain.llms import HuggingFaceHub #huggingface_hub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import mlflow
import mlflow.pyfunc
import mlflow.langchain

import warnings
warnings.filterwarnings("ignore")

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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' #'dummy_key' # set up tocken in settings, huggingface profile


if __name__=="__main__":
    
    print("Inside Experiment 1")
    mlflow.set_experiment(experiment_name="Machine Q&A Experiment")
    with mlflow.start_run():
        model_info = mlflow.transformers.log_model(
            transformers_model=transformers.pipeline(model="microsoft/DialoGPT-medium"),
            artifact_path="chatbot",
            input_example="Hi there!"
        )
        # Load as interactive pyfunc
        chatbot = mlflow.pyfunc.load_model(model_info.model_uri)
        #make predictions
        print(chatbot.predict("What is the best way to get to America?"))
    
    print("Inside Experiment 2")
    mlflow.set_experiment(experiment_name="Machine Translation Experiment")
    with mlflow.start_run():
        question= "Hello, my name is XYZ. I live in ABC, Canada!"
        template1 = """Translate everything you see after this into French: {question}"""
        prompt1 = PromptTemplate(template=template1,input_variables=["question"])
        template2 = """Translate everything you see after this into German: {question}"""
        prompt2 = PromptTemplate(template=template2, input_variables=["question"])
        
        myllm = HuggingFaceHub(
            repo_id= "google/flan-t5-small",
            model_kwargs={"temperature":0.5, "max_length":64}
            )
        
        my_llm_chn1 = LLMChain(prompt=prompt1, llm=myllm)
        print(my_llm_chn1.run(question))

        my_llm_chn2 = LLMChain(prompt=prompt2, llm=myllm)
        print(my_llm_chn2.run(question))

        #mlflow.langchain.log_model(lc_model=my_llm_chn1,artifact_path="model",input_example="english-to-french-chain-gpt-3.5-turbo-1")

        '''
        model_info = mlflow.langchain.log_model(
            lc_model=my_llm_chn2,
            artifact_path="model2",
            input_example="english-to-german"
        )

        model_info = mlflow.langchain.log_model(
            lc_model=my_llm_chn,
            artifact_path="models",
            input_example="english-to-french-chain-gpt-3.5-turbo-1"
            )

        english_to_french_udf = mlflow.pyfunc.spark_udf(
            spark=spark,
            model_uri="models:/english-to-french-chain-gpt-3.5-turbo-1/1",
            result_type="string"
        )
        english_df = spark.createDataFrame([("What is MLflow?",)], ["english_text"])

        french_translated_df = english_df.withColumn(
            "french_text",
            english_to_french_udf("english_text")
        ) 
        '''
