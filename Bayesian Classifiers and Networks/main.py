from functools import reduce
import pandas as pd
import pprint
class Classifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None

    def __init__(self,filename=None, class_attr=None ):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.class_attr = class_attr

    '''
        probability(class) =    How many  times it appears in column
                             __________________________________________
                                  count of all class attribute
    '''
    def calculate_priori(self):
        class_values = list(set(self.data[self.class_attr]))
        class_data =  list(self.data[self.class_attr])
        for i in class_values:
            self.priori[i]  = class_data.count(i)/float(len(class_data))
        print ("Priori Values: ", self.priori)

    '''
        Here we calculate the individual posterior probabilites 
        P(outcome|feature) =   P(Likelihood of feature) x Prior prob of outcome
                               ___________________________________________
                                                    P(feature)
    '''
    def calculate_posterior(self, attr, attr_type, class_value):
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])
        total =1
        for i in range(0, len(data_attr)):
            if class_data[i] == class_value and data_attr[i] == attr_type:
                total+=1
        return total/float(class_data.count(class_value))

    '''
        Here we calculate Likelihood of Evidence and multiple all individual probabilities with priori
        (Outcome|Multiple Evidence) = P(Evidence1|Outcome) x P(Evidence2|outcome) x ... x P(EvidenceN|outcome) x P(Outcome)
                                       -----------------------------------------------------------------------------------
                                                     P(Multiple Evidence)
    '''
    def calculate_conditional_probabilities(self, hypothesis):
        for i in self.priori:
            self.cp[i] = {}
            for j in hypothesis:
                self.cp[i].update({ hypothesis[j]: self.calculate_posterior(j, hypothesis[j], i)})
#        print ("\nCalculated Conditional Probabilities: \n")
#        pprint.pprint(self.cp)

    def classify(self):
        print ("Result: ")
        mx = -1
        for i in self.cp:
            val = reduce(lambda x, y: x*y, self.cp[i].values())*self.priori[i]
            print (i, " ==> ", val )
            if val>mx:
                mx = val
                ans = i

        return ans

    def test_predictions(self,df):
        num_data = 0
        num_correct = 0
        for index,row in df.items():
            self.hypothesis = row
            self.calculate_conditional_probabilities(self.hypothesis)
            label = self.classify()
            print(label)
            for key in row:
                if key=='Play':
                    val = row[key]

            if label == val:
                num_correct += 1
            num_data += 1
        print(num_correct, num_data)
        return round(num_correct/num_data, 2)


if __name__ == "__main__":
    c = Classifier(filename="weather_train.csv", class_attr="Play" )
    c.calculate_priori()

    df_test = pd.read_csv('weather_test.txt',sep='\s+').to_dict(orient= 'index')
    print("Accuracy calculation on test data:")
    print("Accuracy:" , str(c.test_predictions(df_test)*100.0) + '%')

    c.hypothesis1 = {"Outlook":'sunny', "Temp":"high", "Humidity":'high' , "Windy":'true'}
    c.hypothesis2 = {"Outlook":'sunny', "Temp":"high", "Humidity":'mild' , "Windy":'false'}
    c.hypothesis3 = {"Outlook":'rainy', "Temp":"mild", "Humidity":'mild' , "Windy":'true'}
    c.hypothesis4 = {"Outlook":'overcast', "Temp":"cool", "Humidity":'normal' , "Windy":'true'}

    c.calculate_conditional_probabilities(c.hypothesis1)
    ans1 = c.classify()
    print("final classification of this sample is:", ans1)
    c.calculate_conditional_probabilities(c.hypothesis2)
    ans2 = c.classify()
    print("final classification of this sample is:", ans2)
    c.calculate_conditional_probabilities(c.hypothesis3)
    ans3 = c.classify()
    print("final classification of this sample is:", ans3)
    c.calculate_conditional_probabilities(c.hypothesis4)
    ans4 = c.classify()
    print("final classification of this sample is:", ans4)
