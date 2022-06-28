
## FaceID App

This is a facial recognition and verification app using Deep Learning with Tensorflow which is based on the paper: Siamese Neural Networks for One-Shot Image Recognition. The model is integrated into an app using Kivy App. 
## WorkFlow

**Building a Siamese Model**

- Install and import required dependencies.
- Set GPU growth to avoid out of memory errors.
- Create folder structures and set os path.
- Collect dataset for positive, negatives and anchors
- Augment the Data (optional)
- Load and Preprocess the images
- Build and Train and test partition using our preprocess function 
- Model Engineering- Build Embedding Layer
- Build Distance Layer
- Build Siamese Model
- Train the Model
- Evaluate the Model
- Make Predictions
- Save the Model
- Make real time Predictions

**Building The Kivy App**

- Setup app folder 
- Install Kivy
- Setup Validation Folder
- Create custom layer module
- Bring H5 module
- Import dependencies for kivy
- Build Layout
- Build update function and render webcam
- Bring over preprocessing function
- Bring over verification function
- Update verification function to handle new paths and save current frame
- Update verification function to set verified text
- Link verification function to button 
- Setup Logger
## Tech Stack

**Language Used:** Python

**IDE Used:** Jupyter Notebook , VS Code


## Deployement

To deploy this project from the app folder run

```bash
  python faceid.py
```
 


## Special thanks to

 - [@NicholasRenotte](https://www.youtube.com/c/NicholasRenotte)
 - [Reference Paper: Siamese Neural Networks for One-shot Image Recognition by Gregory Koch, Richard Zemel and Ruslan Salakhutdinov](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
 
 


## Authors

- [@tejasrathod](https://www.linkedin.com/in/tejas-rathod-923187189/)



## License

[MIT](https://github.com/TejasARathod/FaceID-APP/blob/65b9997a498d4361ecabe4636b4c50c5fec3a7f9/LICENSE)


## Face App Preview

![](https://github.com/TejasARathod/FaceID-APP/blob/271d79103ecf97f218445b639ac5bd267248e743/1.png)


![](https://github.com/TejasARathod/FaceID-APP/blob/271d79103ecf97f218445b639ac5bd267248e743/2.png)



