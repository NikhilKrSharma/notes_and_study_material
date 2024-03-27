# Quick Notes







# From RAMIT
One of the main issues in learning LLMs is the lack of structured course on what needs to be learned. Below is the path I followed to gain some insights into LLMs. 
 
**First is clearing the basics**:  
[NLP](https://youtube.com/playlist?list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX&si=w3MxhYxUF85BoUWm)  
[RNN, LSTM, Transformers](https://youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn&si=w7N3dYfmj2EdBVB4)

Once you have the basics in place, it is time to shift gears:  
**Framework**: "There are multiple frameworks available for using LLMs, such as LangChain or LlamaIndex. I have been focusing on [LangChain](https://www.youtube.com/playlist?list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar) by Krish Naik.

**Prompt Engineering**: In one line, Prompt engineering involves designing input in such a way to get the desired output from LLMs. Video on this is available on the above link.

**RAGs and VectorDB**: LLMs are trained on a huge amount of data, but for your specific use case, that data might not be available. To address this, you may want to augment data for the LLMs so that they can provide relevant responses. The data is stored in the form of a vector in a database. Some examples of such VectorDBs are ChromaDB, Pinecorn, and Weaviate. 

[RAG+Langchain: Easy AI/Chat for your Docs by pixegami](https://www.youtube.com/watch?v=tcqEUSNCn8I)

**Model Finetuning**: I see this as the most difficult part. Currently, there are two methods which are most popularly being used finetuning the LLMs parameters.  
- LoRA -> Low-Rank Adaptation  
- QLoRA -> Quantized Low-Rank Adaptation  

Some interesting blogs on them:  
- https://abvijaykumar.medium.com/fine-tuning-llm-parameter-efficient-fine-tuning-peft-lora-qlora-part-1-571a472612c4
- https://abvijaykumar.medium.com/fine-tuning-llm-parameter-efficient-fine-tuning-peft-lora-qlora-part-2-d8e23877ac6f
- https://cameronrwolfe.substack.com/p/easily-train-a-specialized-llm-peft  

**Deployment**: Only one I have seen till now is AWS Bedrock. Haven’t gone through this part yet.
 
Hope this helps someone who is trying to learn LLMs. There is a lot of interesting stuff happening in this space, so you have to keep yourself updated. There are a lot more resources I used, but could only find these from my history.