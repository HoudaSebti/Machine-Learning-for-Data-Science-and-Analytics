from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def get_scaler(fitting_set):
    scaler = StandardScaler()
    scaler.fit(fitting_set)
    return scaler

if __name__ == "__main__":    

    mnist = fetch_mldata('MNIST original', data_home="data")
    print(mnist.data.shape)
    print(mnist.target.shape)
    
    train_img, test_img, train_label, test_label = train_test_split( mnist.data, mnist.target, test_size=1/7.0, random_state=0)
    scaler = get_scaler(train_img)
    train_img = scaler.transform(train_img)
    test_img = scaler.transform(test_img)
    pca = PCA(.95)
    print("fitting PCA on the training set")
    pca.fit(train_img)
    print("number of prinicipal components for training set: ", pca.n_components_)