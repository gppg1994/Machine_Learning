from numpy import zeros


def featureNormalize(X):
    X_norm = X
    cols = int(X.size / len(X))
    mu = zeros((1, cols))
    sigma = zeros((1, cols))
    '''Normalizing data'''
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    X_norm=(X-mu)/sigma
    return [X_norm,mu,sigma]
