
##Poms is an AI model manager. 

The goal is serve third party apps local models and information to reduce the need for model storage duplication for each app.

###The problems this solves:

1) **Drive space**: Many AI interfaces contain a /models directory, and often multiple software installations will utilize the same model files, using a lot of drive space
2) **Ease Development**: Individual tools have to juggle downloading and installing these models. This can simplify that process and allow third party developers to focus on their app functionality
3) **Security**: A single point of ingress, auditable. Could be extended to include policy based model access
4) **Improves discovery**, Description / links to Github & Hugging Face 

### General Architecture
Front end  [[Design Specification](http://example.com "Title")]
- Lightweight Desktop widget
- View & Delete installed models
- Browse models & install custom

Backend [[Design Specification](http://example.com "Title")]
- Local API (third party app request model by name or MD5 and Poms will return path or begin download while returning state information to app)
- Manage storage of models

## Questions

- What is the least friction for third party developers to query model states? Environment variables? Local API
- What features would provide the most value to simplify third party developer effort?
- What simplifies and provides the best value to end users? Already installing this as a pre-requisite app is a bit of friction. 
- What license is best for this? 

Design Spec

![image](https://user-images.githubusercontent.com/654993/194750260-830c1500-736c-43fc-9cdd-7b11325fb909.png)

![image](https://user-images.githubusercontent.com/654993/194750242-2f62edcd-1e42-42dc-945a-7793ebd39701.png)

![image](https://user-images.githubusercontent.com/654993/194750284-23f1dc46-654c-430e-a511-c93943357893.png)
