from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.


def index(request):
    return HttpResponse("questions index.")

def get_params(request):
	return render(request,'questions/test.html')


def search(request):
	print("not cached....")
	page=request.GET['page']
	pagesize=request.GET['pagesize']
	order=request.GET['order']
	minvote=request.GET['minvote']
	maxvote=request.GET['maxvote']
	tagged=request.GET['tagged']
	#print(order)
	#return HttpResponse("Search results:")
	titles = stackapi(rpage=page,rpagesize=pagesize,rorder=order,rminvote=minvote,rmaxvote=maxvote,rtagged=tagged)
	return render(request,'questions/results.html',{'order':order,'titles':titles})


def stackapi(rpage="1",rpagesize="1",rfromdate="",rtodate="",rorder="desc",rminvote="0",rmaxvote="10000",rtagged=""):
	print("hello again, world")
	
	page= rpage
	pagesize=rpagesize
	fromdate=rfromdate
	todate=rtodate
	order=rorder
	minvote=rminvote
	maxvote=rmaxvote
	tagged=rtagged
	
	param_query='https://api.stackexchange.com/2.3/questions?page='+page+'&pagesize='+pagesize+'&fromdate='+fromdate+'&todate='+todate+'&order='+order+'&min='+minvote+'&max='+maxvote+'&sort=votes&tagged='+tagged+'&site=stackoverflow'
	r = requests.get(param_query)
	#print(r.content)
	#print(type(r.content)) 
	#print(type(json.loads(r.content)))
	#print(json.dumps(json.loads(r.content),indent=4))

	dict_questions = json.loads(r.content)
	#print(type(dict_questions["items"]))
	result=[]
	for l in dict_questions["items"]:
		#print(l["title"])
		result.append(l["title"])
	#return dict_questions["items"]
	return result