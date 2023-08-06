import numpy as np
import pandas as pd


class TESI():
    def __init__(self, input, Equation='Euc_p1', start=0.01,augmentation_factor=10):
        super(TESI, self).__init__()
        self.input=input
        if not isinstance(self.input, pd.DataFrame):
            raise TypeError("input must be a pandas DataFrame")
        self.X=self.input.T.values
        self.start=start
        self.Equation=Equation
        self.augmentation_factor=augmentation_factor
        self.Equations={'Euc_p1': lambda x,x2: (x/x2) , #linear interpolation {y1 + ((x-x1) / (x2-x1)) * (y2-y1)}
                        'Euc_p2': lambda x,x2: (pow(x,2)/pow(x2,2)) ,
                        'Euc_p3': lambda x,x2: (pow(x,3)/pow(x2,3)),
                        'Euc_Log': lambda x,x2: (np.log(x+1)/np.log(x2+2))}
        '''
        Parameters:
        input: pandas dataframe of m_samples and n_features.
        X: (array) The input array to interpolate. Its can be of 1D or nD shape.
        start: (float), default=0.01, The starting value of the sequence. 
        stop: (int), default=1, The end value of the angle's sines vector. Sould be always 1 because the angle's max sine is 1. 
        augmentation_factor: (int), default (0.01), the number of times the data is augmented. should be from 0 to infinity.
        Equation: (formula), default='Euc_p1', Either the Euclidian or the trasnformed Euclidian formulas. 
        Equations: dictionary of interpolation formulas.
        Euc_p1: the linear polynomial.
        Euc_p2: the quadratic polynomial. 
        Euc_p3: the cubic polynomial.
        Euc_Log: the log transformed euclidian formula. 
        
        '''
        
    # vector interpolator function 
    def interpolate_vector(self, X):
        # calculate the opposites array W
        W=np.diff(X, axis=0)
        W=W.reshape(W.shape[0],1)
        # initiate the angle's sines vector using the start, stop, and num arguments 
        A=np.array(np.linspace(start=0.01, stop=1, num=10))
        # adjacent
        # apply the Pythagoras formula to find the angle's adjacent V.
        V=np.sqrt(np.square(W/A.T)-np.square(W))
        # apply the Euclidean interpolation formula (EIF) or the transgormed EIF to find Y=f(x,y).
        V=self.Equations[f'{self.Equation}'](x=V,x2=V.max())
        # reverse the V array axes
        V_R=np.apply_along_axis(lambda x: x[::-1],1,V)
        # reshape the input vector X to array with shape (n samples, m features)
        X_T=X[:-1].reshape(X.shape[0]-1,1)
        # Y= (Vi/V max)*W 
        Y= V_R*W
        # Y= ((Vi/V max)*W)+Y0
        Y=X_T+Y
        # flatten Y to have shape (n samples, )
        Y=Y.flatten()
        return Y
    
    # matrix interpolator function 
    def interpolate_matrix(self):
        # apply the interpolation on all the input array
        return np.array([TESI(self.input).interpolate_vector(x) for x in self.X])

    # array output function 
    def arr(self):
        if self.X.ndim == 1:
            output=TESI(self.input).interpolate_vector(self.X)
        else:
            output=TESI(self.input).interpolate_matrix()
        return output
    
    # pd DataFrame output function 
    def pd_frame(self, save=False):
        '''
        save: default= False. 
        if save is True, the pandas dataframe will be saved in the work environment directory. 
        '''
        output=pd.DataFrame(TESI(self.input).arr()).T
        output.columns=self.input.columns
        if save ==True:
            output.to_excel('New_dataframe.xlsx', index=False)
        if save ==False:
            output
        return output




