AI model manager. (will be, in development)

[ README.md ]
[[ Frontend Specification ](spec/frontend.md "Frontend Spec")]
[[ Backend Specification ](spec/backend.md "Backend Spec")]

Pons improves user experience by reducing duplication of models stored locally. Eases developer access to AI models by returning the local path to the model or initiating download of the model. Linux / MacOS / Windows support planned

![image](https://user-images.githubusercontent.com/654993/194756455-7d87bb76-24e5-4d4b-b046-8f5a656f63b7.png)

### The problems this solves:

1) **Drive space**: Many AI interfaces contain a /models directory, and often multiple software installations will utilize the same model files, using a lot of drive space
2) **Ease Development**: Individual tools have to juggle downloading and installing these models. This can simplify that process and allow third party developers to focus on their app functionality
3) **Security**: A single point of ingress, auditable. Could be extended to include policy based model access
4) **Improves discovery**, Description / links to Github & Hugging Face 

### General Architecture
Front end  [[Frontend Specification](http://example.com "Title")]
- Lightweight Desktop widget
- View & Delete installed models
- Browse models & install custom

Backend [[Backend Specification](http://example.com "Title")]
- Local API (third party app request model by name or MD5 and Poms will return path or begin download while returning state information to app)
- Manage storage of models

## Questions

- What is the least friction for third party developers to query model states? Environment variables? Local API
- What features would provide the most value to simplify third party developer effort?
- What simplifies and provides the best value to end users? Already installing this as a pre-requisite app is a bit of friction. 
- What license is best for this? 

