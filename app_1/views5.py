from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from app_1.models import Staff_Access
from campaign.models import Order_notifications, Vendor_notifications
from vendor_dashboard_app.models import vendor_registration_table
from django.http import JsonResponse
from django.core import serializers



def all_notification(request, template='all_notification.html', page_template='all_notification_new.html'):
    all_Order_notifications = Order_notifications.objects.order_by('-Notification_time')
    qty_all_Order_notifications = all_Order_notifications.count()
    context = {
        'all_Order_notifications':all_Order_notifications,
        'qty_all_Order_notifications':qty_all_Order_notifications,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)




def vendor_all_notification(request, template='vendor_all_notification.html', page_template='vendor_all_notification_new.html'):
    all_Order_notifications = Vendor_notifications.objects.order_by('-Notification_time')
    qty_all_Order_notifications = all_Order_notifications.count()
    context = {
        'all_Order_notifications':all_Order_notifications,
        'qty_all_Order_notifications':qty_all_Order_notifications,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)




@csrf_exempt
def get_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team

        print(user_of_deshboard_now)
        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        print(get_Staff_Access)

        new_thiks = Order_notifications.objects.order_by('-Notification_time')[:5]
        print(new_thiks)

        a = new_thiks.count()
        print(a)


        # new_thiks = base_notifications.objects.exclude(Notification_stuff = get_Staff_Access)
        # new_thiks = base_notifications.objects.filter(Notification_stuff__in = get_Staff_Access.id)
        # print('new_thiks')
        # print(new_thiks)

        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def get_vendor_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team

        print(user_of_deshboard_now)
        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        print(get_Staff_Access)

        new_thiks = Vendor_notifications.objects.order_by('-Notification_time')[:5]
        print(new_thiks)

        a = new_thiks.count()
        print(a)

        # new_thiks = base_notifications.objects.exclude(Notification_stuff = get_Staff_Access)
        # new_thiks = base_notifications.objects.filter(Notification_stuff__in = get_Staff_Access.id)
        # print('new_thiks')
        # print(new_thiks)

        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)


def upload_vendor_Store_details_notification(request, pk):
    print(pk)

    vendor_registration_table_get = vendor_registration_table.objects.get(id=pk)
    return redirect('upload_vendor_Store_details', vendor_registration_table_get.vendor_phone_no)




@csrf_exempt
def get_notification_qty(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team

        print(user_of_deshboard_now)
        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        print(get_Staff_Access)

        new_thiks = Order_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')[:5]
        print(new_thiks)


        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def vendor_get_notification_qty(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team

        print(user_of_deshboard_now)
        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        print(get_Staff_Access)

        new_thiks = Vendor_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')[:5]
        print(new_thiks)


        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def make_seen_notification(request):
    print('jiji')
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')
    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)
        new_thiks = Order_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')

        for i in new_thiks:
            i.Notification_stuff.add(get_Staff_Access)
        return HttpResponse(True)




@csrf_exempt
def vendor_make_seen_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)
        new_thiks = Vendor_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')

        for i in new_thiks:
            i.Notification_stuff.add(get_Staff_Access)
        return HttpResponse(True)

