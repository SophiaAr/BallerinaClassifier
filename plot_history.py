from matplotlib import pyplot as plt

def plot(history, from_epoch = 0):

    try:
        acc = history.history['acc'][from_epoch:]
        val_acc = history.history['val_acc'][from_epoch:]
        
        # summarize history for accuracy
        plt.plot(acc)
        plt.plot(val_acc)
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
    except:
        print('There is no accuracy log in history variable')
    
    try:
        loss = history.history['loss'][from_epoch:]
        val_loss = history.history['val_loss'][from_epoch:]
        
        # summarize history for loss
        plt.plot(loss)
        plt.plot(val_loss)
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
    except:
        print('There is no loss log in history variable')
