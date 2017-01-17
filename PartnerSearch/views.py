import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from PartnerSearch.forms import InstForm,TestForm
from PartnerSearch.models import Country, Institution, SubmitRequest, UserAttribute, Programme


def register(request):
    return render(request, 'registration/registration.html',{})

@login_required()
def profile(request):
    pk = request.user.pk
    userAtr = UserAttribute.objects.get(pk=pk)
    page_header=request.user.last_name+" " + request.user.first_name
    page_desc=userAtr.contact_email

    return render(request, 'registration/profile.html',{'username':userAtr.fullname,
                                                        'page_header':page_header,
                                                        'page_desc':page_desc})

@login_required()
def add_institution(request):
    page_header="Add Institution"
    page_desc="You have to 'add Institution' before use the tool' "

    countries = Country.objects.all();
    print str(request.user) + str(request.user.id)
    print 'Add institution'
    if request.POST:
        print 'POST'
        inst_name = request.POST['institution_name']
        dep_name = request.POST['department_name']
        inst_number = request.POST['inst_number']
        inst_country = request.POST['country']
        inst_city = request.POST['city']
        inst_website = request.POST['inst_website']
        # inst_contact = request.POST['inst_contact']
        # inst_email = request.POST['inst_email']
        print inst_name+' 2-'+inst_number+'3- '+inst_website+'4- '+ inst_country

        i = Institution(i_user=request.user,country_id=inst_country,institution_name=inst_name,
                    institution_department=dep_name,erasmusCN= inst_number, website=inst_website)
        i.save()


    inst_form = InstForm()
    return render(request, 'forms/addInstitution.html', {'page_header':page_header,
                                                         'page_desc':page_desc,
                                                         'form':inst_form,
                                                         'countries':countries,
                                                         })


def exchange(request):
    institutions = Institution.objects.filter(i_user=request.user)
    if request.POST:
        inst = request.POST['inst']
        print inst
        sr = SubmitRequest(sr_user=request.user, sr_institution_id=inst,sr_program_id=1,
                           type_of_Submit='A')
        sr.save()


    return render(request, 'forms/formExchange.html', {'institutions':institutions})


def exchangeRequest(request):
    page_header="Submit a request for partner search."
    page_desc=""
    description = "Short summary of the request (specific programms of study, international exchange etc, 500 words)"
    institutions = Institution.objects.filter(i_user=request.user)

    if request.POST:
        inst = request.POST['inst']
        inst_desc = request.POST['inst_desc']
        inst_date = request.POST['inst_date']
        print inst+" "+inst_desc
        # i = Institution.objects.get(pk = inst)
        i = get_object_or_404(Institution, pk=inst)
        print 'date'+inst_date

        date = datetime.datetime.strptime(inst_date,"%d/%m/%Y").strftime('%Y-%m-%d')
        print date
        # print i
        # print ii
        sr = SubmitRequest(sr_user=request.user, sr_institution=i,sr_program_id=1,summary=inst_desc,
                           interest_Expected=date);
        sr.save()


    return render(request, 'forms/exchangeRequest.html', {'page_header':page_header,
                                                          'page_desc':page_desc,'description':description,
                                                          'institutions':institutions})



def funded(request):
    page_header="Partner Invitations for EU funded projects"
    page_desc="(HORIZON, ERASMUS+, other)"
    institutions = Institution.objects.filter(i_user=request.user)
    programs = Programme.objects.exclude(id = 1)

    if request.POST:
        inst = request.POST['inst']
        prog = request.POST['prog']
        picNum = request.POST['picNum']
        desc = request.POST['desc']

        # print 'inst-' + inst + '\nprog-' + prog + '\npicNum-' + picNum + '\ndesc-' +desc

        sr = SubmitRequest(sr_user=request.user, sr_institution_id=inst,sr_program_id=prog,
                           pic_number=picNum,
                           type_of_Submit='I',summary=desc)
        sr.save()

    # countries = Country.objects.all();


    return render(request, 'forms/formFunded.html', {'page_header':page_header,
                                                     'page_desc':page_desc,
                                                     'institutions':institutions,
                                                     'programs':programs})


def fundedRequest(request):
    page_header="Partner Invitations for EU funded projects"
    page_desc="(HORIZON, ERASMUS+, other)"
    programmes = Programme.objects.all()
    institutions = Institution.objects.filter(i_user=request.user)

    if request.POST:
        inst = request.POST['inst']
        prog = request.POST['prog']
        picNum = request.POST['picNumber']
        typeOfPart = request.POST['typeOfPart']
        inst_date = request.POST['inst_date']
        inst_date = request.POST['inst_date']
        # print inst+" "+inst_desc

        sr = SubmitRequest(sr_user=request.user, sr_institution_id=inst,sr_program_id=prog,
                           pic_number=picNum,
                           type_of_Submit='A',summary=desc)
        sr.save()


    return render(request, 'forms/fundedRequest.html', {'page_header':page_header,'typeOfPart':typeOfPart,
                                                        'page_desc':page_desc,
                                                        'institutions':institutions,
                                                        'programmes':programmes})