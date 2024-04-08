# Quick Notes



### Bucket (To be finished)
1. [AI – 4 Every 1](https://youtu.be/jSgdL1zX4h8?t=21117)
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Handy Code Snippets

<details>
    <summary>Animation</summary>
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    # Generate Animation
    # Set the plot up
    fig = plt.figure()
    ax = plt.axes()
    plt.title('Sale Price vs Living Area')
    plt.xlabel('Living Area in square feet (normalised)')
    plt.ylabel('Sale Price ($)')
    plt.scatter(x[:,1], y, color='red')
    line, = ax.plot([], [], lw=2)
    annotation = ax.text(-1, 700000, '')
    annotation.set_animated(True)
    plt.close()

    # Generate the animation data
    def init():
        line.set_data([], [])
        annotation.set_text('')
        return line, annotation

    # Animation function. This is called sequentially
    def animate(i):
        x = np.linspace(-5, 20, 1000)
        y = past_thetas[i][1]*x + past_thetas[i][0]
        line.set_data(x, y)
        annotation.set_text('Cost = %.2f e10' % (past_costs[i]/10000000000))
        return line, annotation

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=0, blit=True)
    anim.save('animation.gif', writer='imagemagick', fps = 30)


    # Display the animation...
    import io
    import base64
    from IPython.display import HTML

    filename = 'animation.gif'

    video = io.open(filename, 'r+b').read()
    encoded = base64.b64encode(video)
    HTML(data='''<img src="data:image/gif;base64,{0}" type="gif" />'''.format(encoded.decode('ascii')))
</details>

<details>
    <summary>Text to be shown along the expand button</summary>
    Main text goes here which will be displayed when the  user clicks on the expand button.
</details>



<br>
<br>
<br>

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