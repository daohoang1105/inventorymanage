# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from urllib import response
from .forms import ManageFormOuT, ManageForm
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import os
from .models import AllSparePart, SparePartOutRecord, SparePartOutRequest, Upload, User
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import datetime
import csv

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def sptable(request):
    sp = AllSparePart.objects.all()
    sprequest = SparePartOutRequest.objects.all()

    context = {'sp':sp,'sprequest':sprequest}
    return render(request,'home/sptable.html', context)

@login_required(login_url="/login/")
def sptablegoodnew(request):
    sp = AllSparePart.objects.all()
    sprequest = SparePartOutRequest.objects.all()
    context = {'sp':sp,'sprequest':sprequest}
    return render(request,'home/sptablegoodnew.html', context)

@login_required(login_url="/login/")
def sptablefailscrap(request):
    sp = AllSparePart.objects.all()
    sprequest = SparePartOutRequest.objects.all()
    context = {'sp':sp,'sprequest':sprequest}
    return render(request,'home/sptablefailscrap.html', context)

@login_required(login_url='login')
@xframe_options_exempt
def uploadfromfile(request):
    sprequest = SparePartOutRequest.objects.all()
    try:
        filehere = Upload.objects.get(id=1)
    except:
        filehere = None

    if request.method == 'POST':
        upload = Upload.objects.create(
            user = request.user,
            file = request.FILES.get('files')
        )
        filename = request.FILES.get('files')
        user = request.user
        try:
            autoadd(filename,user)
        except:
            return redirect('uploadfromfileerror')
        return redirect('uploadfromfilesuccess')

    
    context = {'filehere':filehere,'sprequest':sprequest}
   
    return render(request,'home/uploadfromfile.html', context)

@login_required(login_url="/login/")
def uploadfromfilesuccess(request):
    sp = AllSparePart.objects.all()
    context = {'sp':sp}
    return render(request,'home/uploadfromfilesuccess.html', context)

@login_required(login_url="/login/")
def uploadfromfileerror(request):
    sp = AllSparePart.objects.all()
    context = {'sp':sp}
    return render(request,'home/uploadfromfileerror.html', context)

def autoadd(filename,user):
    filename0 = str(filename).replace(' ','_')
    dir0 = os.path.join(os.getcwd(), "staticfiles/mediaurl/fileupload")
    dir1 = os.path.join(dir0,filename0)

    df0 = pd.read_excel(dir1)
    df0.columns = [c.replace(' ', '_') for c in df0.columns]
    df0.columns = [c.replace('/', '') for c in df0.columns]
    df0 = df0.fillna('000')
    for i in range(0,df0.shape[0]):
        AllSparePart.objects.create(
                remainQTY=df0.loc[i,"Remaining_Qty"],
                consumQTY=df0.loc[i,"Consump_Qty_"],
                actualQTY = df0.loc[i,"Actual_Qty"],
                remark = df0.loc[i,"Remark"],
                transitWay=df0.loc[i,"Transporation_way_(DHL_Air_Sea)"],
                batch = df0.loc[i,"#_Batch"],
                invoice = df0.loc[i,"Invoice"],
                sender = df0.loc[i,"Sender"],
                warehouse = df0.loc[i,"Warehouse_\n(HN,DN,KH,HCM)"],
                deliverDate = df0.loc[i,"Delivery_date_"],
                productDescription = df0.loc[i,"Product_Description"],
                serialNumber = df0.loc[i,"SN"],
                csceHWMO = df0.loc[i,"Central_inverter,_string_inverter,_Comunication_device,_ESS_,_Hybird__inverter_,_wind_Converter_,_MV_device,_Other)"],
                sparePartType = df0.loc[i,"Spare_part_type_(product_spare_part)"],
                goodStatus = df0.loc[i,"Goods_status_(newgood)"],
                partCode = df0.loc[i,"Part_Code"],
                user = user
            )
    return redirect('uploadfromfilesuccess')



@login_required(login_url='login')
def spmanage(request,pk):
    sp = AllSparePart.objects.all()
    spare = AllSparePart.objects.get(id = pk)
    spareOut = spare.sparepartoutrecord_set.all()
    spareOutRequest = spare.sparepartoutrequest_set.all()

    requestsuccess = 2
    remainqty = spare.remainQTY
    sprequest = SparePartOutRequest.objects.all()
    

    if request.method == 'POST':
        outqty = request.POST.get('outqty')
        try:
            if int(remainqty) >= int(outqty) and int(outqty) > 0 :
                SparePartOutRequest.objects.create(
                    userOutRequestor = request.user,
                    sparePartOut = spare,
                    outqty = request.POST.get('outqty'),
                    outDate = request.POST.get('outDate'),
                    outReceiver = request.POST.get('outReceiver'),
                    outRemark = request.POST.get('outRemark'),
                    file = request.FILES.get('reportfile')
                )
                requestsuccess=0
                return redirect('spmanage', pk=spare.id)
        except:
            requestsuccess=1
    
    if(request.GET.get('mybtn2')):
        # mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')))
        pk = int(request.GET.get('mytextbox'))
        spareOutInRequest = spare.sparepartoutrequest_set.get(id=pk)
        if spareOutInRequest.submitByWm == False:
            spareOutSubmit = SparePartOutRecord.objects.create(
                userOutRequestor = spareOutInRequest.userOutRequestor,
                sparePartGoodOut = spare,
                outqty = spareOutInRequest.outqty,
                outDate = spareOutInRequest.outDate,
                outReceiver = spareOutInRequest.outReceiver,
                outRemark = spareOutInRequest.outRemark,
                outgsp = spareOutInRequest.gsp,
                gspuser = spareOutInRequest.gspuser
            )
            spare.consumQTY += int(spareOutSubmit.outqty)
            spare.remainQTY -= int(spareOutSubmit.outqty)
            spare.save()
            spareOutInRequest.submitByWm = True
            spareOutInRequest.save()
            return redirect('spmanage', pk=spare.id)

    if(request.GET.get('mybtn')):
        # mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')))
        pk = int(request.GET.get('mytextbox'))
        spareOutInRequest = spare.sparepartoutrequest_set.get(id=pk)
        if spareOutInRequest.submitByBoss == False:
            spareOutInRequest.gsp = request.GET.get('mygspbox')
            spareOutInRequest.gspuser = request.user.username
            spareOutInRequest.submitByBoss = True
            spareOutInRequest.save()
            return redirect('spmanage', pk=spare.id)

    if(request.GET.get('deletebtn')):
        pk = int(request.GET.get('mytextbox'))
        deletesp = SparePartOutRequest.objects.get(id=pk)
        if request.user == deletesp.userOutRequestor:
            deletesp.delete()
            return redirect('spmanage', pk=spare.id)

    context = {'sp':sp,'spare':spare,'requestsuccess':requestsuccess,'sprequest':sprequest,'spareOutRequest':spareOutRequest,'spareOut':spareOut}
    return render(request,'home/spmanage.html', context)

@login_required(login_url="/login/")
def upload(request):
    sp = AllSparePart.objects.all()
    sprequest = SparePartOutRequest.objects.all()
    form = ManageForm(initial={'user': request.user})  
    if request.method == 'POST':
        form = ManageForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('sptable')

    context = {'sp':sp,'form':form,'sprequest':sprequest}
    return render(request,'home/upload.html', context)

@login_required(login_url='login')
def updateSpare(request, pk):
    spare = AllSparePart.objects.get(id=pk)
    form = ManageForm(instance=spare)  
    # if request.user.role == 0:
    #     return HttpResponse('<h1>You are not allowed here!</h1>')
    if request.method == 'POST':
        form = ManageForm(request.POST, instance=spare)
        if form.is_valid:
            form.save()
            return redirect('pages')

    context = {'form': form,'spare':spare}
    return render(request, 'home/updatespare.html',context)

@login_required(login_url='login')
def deleteSpare(request, pk):
    spare = AllSparePart.objects.get(id=pk)

    # if request.user == 0:
    #     return HttpResponse('<h1>You are not allowed here!</h1>')

    if request.method == 'POST':
        spare.delete()
        return redirect('pages')
    return render(request, 'home/deletespare.html', {'obj':spare})

@login_required(login_url="/login/")
def outsptable(request):
    sp = SparePartOutRecord.objects.all()
    sprequest = SparePartOutRequest.objects.all()
    context = {'sp':sp,'sprequest':sprequest}
    return render(request,'home/outsptable.html', context)

@login_required(login_url="/login/")
def requestsp(request):
    sprequest = SparePartOutRequest.objects.all()
    droprequest = 0
    requestsuccess = 2
    spareSearch = AllSparePart.objects.all()

    if request.method == 'POST':
        partCode = request.POST.get('SparePartCode')
        goodStatus = request.POST.get('goodStatus')
        outqty = request.POST.get('outqty')
        warehouse = request.POST.get('warehouse')
        print('==',partCode,'==',goodStatus,'==',outqty,'==',warehouse)
        for spare in spareSearch:
            if spare.partCode == partCode and spare.remainQTY >= int(outqty) and spare.warehouse == warehouse and int(outqty)>0 and spare.goodStatus == goodStatus:
                SparePartOutRequest.objects.create(
                    userOutRequestor = request.user,
                    sparePartOut = spare,
                    outqty = request.POST.get('outqty'),
                    outDate = request.POST.get('outDate'),
                    outReceiver = request.POST.get('outReceiver'),
                    # outGSP = request.POST.get('outGSP'),
                    outRemark = request.POST.get('outRemark'),
                    file = request.FILES.get('reportfile')
                )
                requestsuccess = 1
                break
            else:
                requestsuccess = 0

    if(request.GET.get('mybtn2')):
        # mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')))
        pk = int(request.GET.get('mytextbox'))
        data2 = SparePartOutRequest.objects.get(id=pk)
        spareOutInRequest = data2.sparePartOut.sparepartoutrequest_set.get(id=pk)
        if data2.submitByWm == False:
            spareOutSubmit = SparePartOutRecord.objects.create(
                userOutRequestor = spareOutInRequest.userOutRequestor,
                sparePartGoodOut = data2.sparePartOut,
                outqty = spareOutInRequest.outqty,
                outDate = spareOutInRequest.outDate,
                outReceiver = spareOutInRequest.outReceiver,
                # outgsp = request.GET.get('mygspbox'),
                outRemark = spareOutInRequest.outRemark,
                outgsp = spareOutInRequest.gsp,
                gspuser = spareOutInRequest.gspuser
            )
            data2.sparePartOut.consumQTY += int(spareOutSubmit.outqty)
            data2.sparePartOut.remainQTY -= int(spareOutSubmit.outqty)
            data2.sparePartOut.save()
            data2.submitByWm = True
            data2.save()
            # spareOutInRequest.submitByWm = True
            # spareOutInRequest.save()
            return redirect('spmanage', pk=data2.sparePartOut.id)
        else:
            pass

    if(request.GET.get('mybtn')):
        pk = int(request.GET.get('mytextbox'))
        data2 = SparePartOutRequest.objects.get(id=pk)
        spareOutInRequest = data2.sparePartOut.sparepartoutrequest_set.get(id=pk)
        if data2.submitByBoss == False:
                spareOutInRequest.gsp = request.GET.get('mygspbox')
                spareOutInRequest.gspuser = request.user.username
                spareOutInRequest.submitByBoss = True
                spareOutInRequest.save()
                return redirect('spmanage', pk=data2.sparePartOut.id)
        else:
            pass

    context ={'sprequest':sprequest, 'droprequest':droprequest,'requestsuccess':requestsuccess,'spareSearch':spareSearch}
    
    return render(request,'home/requestsp.html', context)

def addgsp(request):
    sp = SparePartOutRecord.objects.all()
    context = {'sp':sp}
    return render(request,'home/addgsp.html', context)

@login_required(login_url='login')
def updateGsp(request, pk):
    spare = SparePartOutRecord.objects.get(id=pk)
    form = ManageFormOuT(instance=spare)  
    # if request.user.role == 0:
    #     return HttpResponse('<h1>You are not allowed here!</h1>')
    if request.method == 'POST':
        form = ManageFormOuT(request.POST, instance=spare)
        if form.is_valid:
            form.save()
            spare.gspuser = request.user.username
            spare.save()
            return redirect('pages')

    context = {'form': form,'spare':spare}
    return render(request, 'home/updategsp.html',context)

def exportcsv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename=Expenses'+ str(datetime.datetime.now()) +'.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','PART CODE','Good status','Spare Part type','csceHWMO','serialNumber','productDescription','deliverDate','warehouse','sender','invoice','batch','transitWay','remark','actualQTY','consumQTY','remainQTY','user'])
    sp=AllSparePart.objects.all()
    for s in sp:
        writer.writerow([s.id,s.partCode,s.goodStatus,s.sparePartType,s.csceHWMO,s.serialNumber,s.productDescription,s.deliverDate,s.warehouse,s.sender,s.invoice,s.batch,s.transitWay,s.remark,s.actualQTY,s.consumQTY,s.remainQTY,s.user])
    return response

def exportoutcsv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition']='attachment; filename=Expenses'+ str(datetime.datetime.now()) +'.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','requestor','spgid','Part code','qty','status','sn','gsp','suby','warehouse'])
    sp=SparePartOutRecord.objects.all()
    for s in sp:
        writer.writerow([s.id,s.userOutRequestor,s.sparePartGoodOut.id,s.sparePartGoodOut.partCode,s.outqty,s.sparePartGoodOut.goodStatus,s.sparePartGoodOut.serialNumber,s.outgsp,s.gspuser,s.sparePartGoodOut.warehouse])
    return response
    
