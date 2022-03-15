from django.http import HttpResponse

# -------------- IMPORTANT -------------- 

# Webhooks being completely ignored due to error 401 unauthorised access (API Key)

# -------------- IMPORTANT -------------- 

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):

        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)


    def handle_payment_intent_succeeded(self, event):

        # intent = event.data.object
        # Stripe 15 

        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)


    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)


    # def handle_payment_intent_create(self, event):

    #     return HttpResponse(
    #         content=f"Webhook received: {event['type']}",
    #         status=200)