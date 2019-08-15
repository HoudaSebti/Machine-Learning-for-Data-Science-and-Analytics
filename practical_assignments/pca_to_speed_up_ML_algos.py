from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

def get_scaler(fitting_set):
    scaler = StandardScaler()
    scaler.fit(fitting_set)
    return scaler

def train_pca(retained_variance, fitting_set):
    pca = PCA(retained_variance)
    print("started fitting PCA...")
    pca.fit(fitting_set)
    print("done fitting PCA...")
    print("number of prinicipal components for the fitting set set: ", pca.n_components_)
    return pca

if __name__ == "__main__":    

    mnist = fetch_mldata('MNIST original', data_home="data")
    print(mnist.data.shape)
    print(mnist.target.shape)
    
    train_imgs, test_imgs, train_labels, test_labels = train_test_split( mnist.data, mnist.target, test_size=1/7.0, random_state=0)
    
    scaler = get_scaler(train_imgs)
    train_imgs = scaler.transform(train_imgs)
    test_imgs = scaler.transform(test_imgs)
        
    pca = train_pca(.95, train_imgs)
    train_imgs = pca.transform(train_imgs)
    test_imgs = pca.transform(test_imgs)
    
    logistic_regr = LogisticRegression(solver = 'lbfgs')
    print("started training the logistic regression classifier...")
    logistic_regr.fit(train_imgs, train_labels)
    print("done training the logistic regression classifier")
    print("test data size: ", test_imgs[0].reshape(1,-1).size)
    print("predicted label for 1st test: ",logistic_regr.predict(test_imgs[0].reshape(1,-1)))
    score = logistic_regr.score(test_imgs, test_labels)
    print("score is: ", score)