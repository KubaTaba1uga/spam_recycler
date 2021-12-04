import logging
from mailboxes.models import MailboxModel, MailboxGuestModel
from reports.models import ReportModel, MessageModel, MessageEvaluationModel


def get_user_guest_mailboxes(user):
    """
    Returns guest mailboxes of a user.
    """
    return (guest_mailbox.mailbox for guest_mailbox in MailboxGuestModel.objects.filter(guest=user).all())


def get_user_owner_mailboxes_query(user):
    return MailboxModel.objects.filter(owner=user).all()


def get_user_owner_mailboxes(user):
    """
    Return owned mailboxes of a user.
    """
    return (owned_mailbox for owned_mailbox in get_user_owner_mailboxes_query(user))


def get_user_owner_mailboxes_tuples(user):
    """
    Return owned mailboxes of a user as tuple
    """
    return ((owned_mailbox.id, owned_mailbox.email_address) for owned_mailbox in get_user_owner_mailboxes_query(user))


def get_mailbox_query(mailbox_id):
    return MailboxModel.objects.filter(pk=mailbox_id).first()


def get_mailbox_owner(mailbox_id):
    """
    Return owner of a mailbox or None if mailbox does not exist
    """
    mailbox = get_mailbox_query(mailbox_id)
    if mailbox:
        return mailbox.owner


def get_mailbox_guests_query(mailbox_id):
    return MailboxGuestModel.objects.filter(mailbox_id=mailbox_id).all()


def get_mailbox_guests(mailbox_id):
    """ Return all guests of mailbox with provided id
    """
    return (guest_mailbox.guest for guest_mailbox in get_mailbox_guests_query(mailbox_id))


def get_guest_mailbox(mailbox_id):
    """
    Return all guest mailboxes of mailbox with provided id
    """
    return (guest_mailbox for guest_mailbox in get_mailbox_guests_query(mailbox_id))


def get_guest(guest_id):
    """
    Return all guest mailboxes of mailbox with provided id
    """

    return MailboxGuestModel.objects.filter(pk=guest_id).first()


def get_user_owner_reports(user):
    """
    Return all reports of user owned mailboxes
    """

    for mailbox in get_user_owner_mailboxes(user):
        for report in mailbox.report.all():
            yield report


def get_user_guest_reports(user):
    """
    Return all reports of user guest mailboxes
    """
    for mailbox in get_user_guest_mailboxes(user):
        for report in mailbox.report.all():
            yield report


def get_mailbox_by_owner(email_address, user):
    return MailboxModel.objects.filter(email_address=email_address, owner=user).first()


def create_report(name, mailbox_id, start_at, end_at):
    return ReportModel.objects.create(
        name=name,
            mailbox_id=mailbox_id,
            start_at=start_at,
            end_at=end_at,
            messages_counter=0)


def create_message(subject, sender, to_recipients,
                   received_at, body, folder, report_id):
    return MessageModel.objects.create(
        subject=subject,
        sender=sender,
        to_recipients=to_recipients,
        received_at=received_at,
        body=body,
        folder=folder,
        report_id=report_id)


def get_report_by_mailbox_and_name(name, mailbox):
    return ReportModel.objects.filter(name=name, mailbox=mailbox).first()


def count_messages_in_report(report):
    return MessageModel.objects.filter(
        report=report).count()


def count_messages_evaluations_in_report(report):
    return MessageEvaluationModel.objects.filter(
        message__report=report).count()


def get_report_by_id_and_owner(report_id, user_id):
    return ReportModel.objects.filter(pk=report_id, mailbox__owner_id=user_id).first()


def validate_report_owner(report_id, user_id):
    return get_report_by_id_and_owner(report_id, user_id)
