from django.views import generic
from django.urls import reverse_lazy
from .models import MailboxModel, MailboxGuestModel
from .mixins import (
    ShowMailboxGuestMixin,
    ShowMailboxOwnerMixin,
    AddMailboxOwnerMixin,
    ValidateMailboxImapMixin,
    PassLoggedUserToFormMixin,
    MailboxOwnerOnlyMixin,
    MailboxOwnerAndGuestOnlyMixin)
from .forms import MailboxCreateForm, MailboxUpdateForm, MailboxAddGuestForm


class MailboxListView(ShowMailboxGuestMixin, ShowMailboxOwnerMixin, generic.ListView):
    template_name = 'mailboxes/mailbox_list_template.html'
    model = MailboxModel


class MailboxCreateView(AddMailboxOwnerMixin, ValidateMailboxImapMixin, generic.CreateView):

    """ Create mailbox if:
        - email server address is valid
        - email address is valid
        - email address password is valid
    """
    template_name = 'mailboxes/mailbox_create_template.html'
    model = MailboxModel
    form_class = MailboxCreateForm


class MailboxEditView(MailboxOwnerOnlyMixin, ValidateMailboxImapMixin, generic.UpdateView):
    template_name = 'mailboxes/mailbox_edit_template.html'
    model = MailboxModel
    form_class = MailboxUpdateForm


class MailboxDetailsView(MailboxOwnerAndGuestOnlyMixin, generic.DetailView):
    template_name = 'mailboxes/mailbox_details_template.html'
    model = MailboxModel
    context_object_name = 'mailbox'


class MailboxDeleteView(generic.DeleteView):
    template_name = 'mailboxes/mailbox_delete_template.html'
    model = MailboxModel
    context_object_name = 'mailbox'
    success_url = reverse_lazy('mailboxes:mailbox_list_url')


class MailboxAddGuestView(PassLoggedUserToFormMixin, generic.CreateView):
    template_name = 'mailboxes/mailbox_add_guest_template.html'
    model = MailboxGuestModel
    form_class = MailboxAddGuestForm
