
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.conf import settings
from django.views import generic
# from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# import pandas


from django.shortcuts import render, redirect
from django.conf import settings
import pandas 
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import os

from .models import Document
from .forms import UploadFileForm

def index(request):
	return render(request,'index.html',{})
# def index1(request):
# 	return render(request,'index1.html',{})
def contact(request):
	return render(request,'contact.html',{})
def about(request):
	return render(request,'about.html',{})
def details(request):
	aaa=Clinicalmanager.objects.all()
	
	return render(request,'details.html',{'aaa':aaa})
def regional(request):
	return render(request,'regional.html',{})
def result(request):
	return render(request,'result.html',{})


def signout(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email,password=password)
		if user:
			print (user)
			login(request,user)
			return HttpResponseRedirect(reverse('about'))
			# return render(request,'about.html', {"msg3":'Login Successfully'})
		else:
			# error="sorry"
			return render(request,'index.html',{"msg2":'UNABLE TO LOGIN '})
	else:
		return render(request,'index.html',{})
	# else:
	#   return render(request,'login.html',{})  
	return render(request,'index.html',{})


def signup(request):
	if request.method=='POST':
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		password = request.POST.get('password')
		email = request.POST.get('email')

		user1=UserProfile.objects.filter(email=email,password=password).exists()
		if not user1:   
			user2=User.objects.create_user(
				username=email,
				password=password,
				)
			
			user_pro=UserProfile.objects.create(
				user=user2,
				email=email,
				password=password,
				mobile=mobile,
				
			)
			user_pro.save()
			return render(request,'index.html',{"msg1":'you are logined'})
		else:
			error='you r already signed'
			return render(request,'index.html',{'error':error})


		# return render(request,'login.html',{"msg1":'you are logined'})
	else:
		return render(request,'index.html',{})
	return render(request,'index.html',{})


def clinicalmanager(request):
	if request.method=="POST":
		nameofdepartment=request.POST.get('nameofdepartment')
		print("nameofdepartment",nameofdepartment)
		partgrp=request.POST.get('partgrp')
		print("partgrp",partgrp)
		descrptn=request.POST.get('descrptn')
		print("descrptn",descrptn)
		dte=request.POST.get('dte')
		print("dte",dte)
		nameofclinicalengr=request.POST.get('nameofclinicalengr')
		print("nameofclinicalengr",nameofclinicalengr)
		nameofhospital=request.POST.get('nameofhospital')
		print("nameofhospital",nameofhospital)
		ceid=request.POST.get('ceid')
		print("ceid",ceid)
		ponumber=request.POST.get('ponumber')
		print("ponumber",ponumber)
		prnumber=request.POST.get('prnumber')
		print("prnumber",prnumber)
		status=request.POST.get('status')
		# print("status",status)

		
		ss=Clinicalmanager.objects.create(
			nameofdepartment=nameofdepartment,
			partgrp=partgrp,
			descrptn=descrptn,
			dte=dte,
			nameofclinicalengr=nameofclinicalengr,
			nameofhospital=nameofhospital,
			ceid=ceid,
			ponumber=ponumber,
			prnumber=prnumber,
			status=status,

			)
		ss.save() 
		# aaa=Clinicalmanager.objects(status1='new').update(status2='approved')	
		
		# if ss:
		# 	x=Areamanager.objects.get(user=user)
		# 	if x.approval:
		# 		print('approve')
		# 		return HttpResponseRedirect(reverse('about'))
		# 	else:
		# 		msg="you are not Approved"
		# 		return render(request,'index', {"error":error})
		# else:
		# 	error="Sorry ,Plz try again"
		# 	return render(request,'index1.html',{})


		return render(request,'about.html',{'ss':ss})
	else:
		return render(request,'index.html')

	return render(request,'index.html',{})

        
def signup1(request):
	if request.method=='POST':
		name = request.POST.get('name')
		print("name",name)
		mobile = request.POST.get('mobile')
		print("mobile",mobile)
		password = request.POST.get('password')
		print("password",password)
		email = request.POST.get('email')
		print("email",email)
		user1=Regional.objects.filter(email=email,password=password).exists()
		if not user1:   
			user2=User.objects.create_user(
				username=email,
				password=password,
				)
			
			user_pro=Regional.objects.create(
				user=user2,
				email=email,
				password=password,
				mobile=mobile,
				
			)
			user_pro.save()
			return render(request,'regional.html',{"msg1":'you are logined'})
		else:
			error='you r already signed'
			return render(request,'index.html',{'error':error})


		# return render(request,'login.html',{"msg1":'you are logined'})
	else:
		return render(request,'regional.html',{})
	return render(request,'regional.html',{})

def log_in1(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email,password=password)
		if user:
			print (user)
			login(request,user)
			return HttpResponseRedirect(reverse('contact'))
			# return render(request,'about.html', {"msg3":'Login Successfully'})
		else:
			# error="sorry"
			return render(request,'about.html',{"msg2":'UNABLE TO LOGIN '})
	else:
		return render(request,'about.html',{})
	# else:
	#   return render(request,'login.html',{})  
	return render(request,'about.html',{})

def contact(request):
	if request.method=="POST":
		k=request.POST.get("feedback")
		print("k",k)
		j=request.POST.get("details")
		print("j",j)
		feedback= Requestforregionalmanager.objects.create(
			feedback=k,details=j,)
		feedback.save()
		print("feedback",feedback)
		print("feedback",feedback)
		return render(request,'index.html')
	else:
		return render(request,'contact.html')

	return render(request,'contact.html')	



def source(request):
	if request.method=="POST":
		k=request.POST.get("feedback")
		print("k",k)
		j=request.POST.get("details")
		print("j",j)
		feedback= SourcingTeam.objects.create(
			feedback=k,details=j,)
		feedback.save()
		print("feedback",feedback)
		print("feedback",feedback)
		return render(request,'index.html')
	else:
		return render(request,'source.html')

	return render(request,'source.html')	

def simple_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'prediction.html', {'form': form})
# def prediction1(request):
# 	return render(request, 'prediction1.html')

def prediction(request):

	path = ('/media/atees/DATA/maneesha/liver/mysite/blog/')
	files = os.listdir(path)
	for file in files:
		if file.endswith('.csv'):
			dataset = pandas.read_csv(path+file)
			print(dataset.shape)

# head
			print(dataset.head(5))

			print(dataset.isnull().any(axis=0))# to check if there any missing values.

			print(dataset.isna().sum()) # check existing null values.

			dataset.fillna(dataset.mean(), inplace=True) #Then fill with mean of the column values.

			print(dataset.isnull().any(axis=0))# again check if there any missing values.


			# descriptions
			print(dataset.describe())

			# class distribution
			print(dataset.groupby('Dataset').size())

			# box and whisker plots
			#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
			#plt.show()

			# histograms
			dataset.hist()
			# plt.show()

			# scatter plot matrix
			scatter_matrix(dataset)
			# plt.show()

			# Split-out validation dataset
			array = dataset.values
			X = array[:,0:9]
			print(X)
			Y = array[:,10]
			print(Y)
			validation_size = 0.20
			seed = 1
			X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
			# Test options and evaluation metric
			seed = 1
			scoring = 'accuracy'
			# Spot Check Algorithms
			models = []
			models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
			models.append(('LDA', LinearDiscriminantAnalysis()))
			models.append(('KNN', KNeighborsClassifier()))
			models.append(('CART', DecisionTreeClassifier()))
			models.append(('NB', GaussianNB()))
			models.append(('SVM', SVC(gamma='auto')))
			# evaluate each model in turn
			results = []
			names = []
			for name, model in models:
				kfold = model_selection.KFold(n_splits=10, random_state=seed)
				cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
				results.append(cv_results)
				names.append(name)
				msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
				print(msg)
			    
			# Compare Algorithms
			fig = plt.figure()
			fig.suptitle('Algorithm Comparison')
			ax = fig.add_subplot(111)
			plt.boxplot(results)
			ax.set_xticklabels(names)
			# plt.show()    

			# Make predictions on validation dataset
			knn = KNeighborsClassifier()
			knn.fit(X_train, Y_train)
			plt.show()    

			predictions = knn.predict(X_validation)
			a = accuracy_score(Y_validation, predictions)
			b = confusion_matrix(Y_validation, predictions)
			c = classification_report(Y_validation, predictions)

			return render(request,'result.html',{'a':a,'b':b,'c':c})

									