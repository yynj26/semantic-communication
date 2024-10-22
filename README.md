### TL;DR 
Check out the /Checkpoint directory, contains: 

Output file and shape at each stage: 

- Semantic Encoder 
- Channel Encodeder
- Channel Decodeder
- Semantic Decoder

And sample input & output file after 3 epochs, more epochs to be come(with better results)

#### Where to make change 

- src/communication : this directory is for all tele-communication function and modules, you can add function here



### Running Command 

#### 1. Training the Model 

python src/train.py --vocab-file europarl/vocab.json --checkpoint-path checkpoints/AWGN --MAX-LENGTH 30 --MIN-LENGTH 4 --d-model 128 --dff 512 --num-layers 4 --num-heads 8 --batch-size 128 --epochs 80

#### 2. Running Performance Evaluation  

python src/main.py --task performance


#### 3. view the transmitted text


python src/main.py --task view_transmitted_text


#### 4.show intermediate data and shapes of tensor files from checkpoints


python src/main.py --task read_log


#### 5.show bleu plot


python src/main.py --task plot_bleu


