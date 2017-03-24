'''
Customer Service dialog creator. Length of dialog is flexible. Each customer question is answered
by a simple phrase. There are no follow up questions, every question-answer pair stands all by itself.
Used for training a CS dialog demo.

Created on 23 mrt. 2017

@author: teno
'''

import numpy as np
import csv

opening = ['Hello. How can I help you?', 'Howdie, what can I do for you?']

c1 = ['My card is stolen', 'I lost my card', 'My credit card was stolen yesterday!']
f1 = ['I\'m sorry to hear that. We will block your card and send you a new one. Is there anything else I can help with?']

c2 = ['I am traveling next month. I want to increase my credit limit.', 'I need more money to spend!', 'At the end of my salary, there always is some month left. Can you help me with that?']
f2 = ['That should be no problem. Is there anything else I can help with?']

c3 = ['I need a mortgage', 'I am going to buy a house', 'How much can I borrow to buy a house?']
f3 = ['Let me transfer you to our mortgage specialists. Is there anything else I can help with?']

c4 = ['What are the tax implications of your Mortgage Special Offer?', 'Do I need to pay tax for fundraising events?']
f4 = ['Let me transfer you to our tax specialists. Is there anything else I can help with?']

c5 = ['What is my current balance?', 'How much money do I have?']
f5 = ['Your current balance is XYZ. Is there anything else I can help with?']

c6 = ['I want to cancel my account', 'I want out', 'Please cancel all my products asap']
f6 = ['I am sorry to hear you want to stop using our services. Is there anything else I can help with?']

startquestions = [{ 'questions' : c1, 'phrases' : f1},
                  { 'questions' : c2, 'phrases' : f2},
                  { 'questions' : c3, 'phrases' : f3},
                  { 'questions' : c4, 'phrases' : f4},
                  { 'questions' : c5, 'phrases' : f5},
                  { 'questions' : c6, 'phrases' : f6}]

close_no = ['no', 'No thank you']
close_yes = ['Yes', 'Yes please.', 'I do have another question.']

ndialogs = 10000
ncustomers = ndialogs/2
if __name__ == '__main__':
    csvfile = csv.writer(open('dialogs.csv', 'wb'), delimiter=';',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvfile.writerow(['dialog','CustomerID','sentence','opening','previous','current','phrase'])
    for n in range(0,ndialogs):
        print("\nDialog:")
        customerID = 'CE-' + str(np.random.randint(1, ncustomers))
        dialoglength = 1
        while (np.random.random() > 0.8 and dialoglength < len(startquestions)):
            dialoglength = dialoglength+1
        dialogsnapshot = {'current' : None }
        print('Agent: ' + np.random.choice(opening))
        dialog = np.random.choice(startquestions, size=dialoglength, replace=False)
        for m in range(1, 1+dialoglength):
            singleqa = dialog[m-1]
            q = np.random.choice(singleqa['questions'])
            a = np.random.choice(singleqa['phrases'])
            if (m == 1): 
                dialogsnapshot['opening'] = q
            dialogsnapshot['previous'] = dialogsnapshot['current']
            dialogsnapshot['current'] = q
            print('Cust: ' + q)
            dialogsnapshot['phrase'] = a
            print('Agent: ' + a)
            if (m < dialoglength):
                print('Cust: ' + np.random.choice(close_yes))
            else:
                print('Cust: ' + np.random.choice(close_no))
            csvfile.writerow([n+1, customerID, m, dialogsnapshot['opening'], dialogsnapshot['previous'], dialogsnapshot['current'], dialogsnapshot['phrase']])

