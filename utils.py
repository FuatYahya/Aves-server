from django.core.mail import EmailMessage
import uuid
from moviepy.editor import VideoFileClip, concatenate_videoclips


class Util():
    '''
    Utils class for the project
    '''
    CLIP_LENGTH = 2
    CLIP_AMOUNT = 5

    def __init__(self) -> None:
        pass

    @staticmethod
    def send_email(data: dict):
        '''
        Send email using params from data dictionary

        :param data: a dict object contaning subjext, body, and to -> recipient  

        :return: True if send success
        '''
        email = EmailMessage(
            subject=data['subject'], body=data['body'], to=data['to'])
        email.send()
        return True

    @staticmethod
    def create_uuid() -> uuid.UUID:
        return uuid.uuid4()

    @staticmethod
    def get_uuid_from_byte(bytes) -> uuid.UUID:
        return uuid.UUID(bytes=bytes)

    @staticmethod
    def get_subclip_offsets(duration: int) -> list:
        # Initializer offset list to hold offsets
        offsets = []
        # Get how many parts can we get from the total clip duration
        parts = int(duration/Util.CLIP_LENGTH)
        # Get equaly distatnt parts by dividing total parts with amount of parts we need
        divs = int(parts/Util.CLIP_AMOUNT)
        # Append offsets by increamenting div times each time
        for i in range(0, parts, divs):
            offset = i * Util.CLIP_LENGTH
            offsets.append(offset)
        return offsets

    @staticmethod
    def get_preview(in_file: str, out_file: str) -> bool:
        '''
        Gets a small preview video from a video file

        :param in_file: input video file path
        :param out_file: output video file path

        :return: True if success
        '''
        clip = VideoFileClip(in_file)
        subclip_offsets = Util.get_subclip_offsets(clip.duration)
        subclips = [clip.subclip(offset, offset+Util.CLIP_LENGTH)
                    for offset in subclip_offsets]
        final_clip = concatenate_videoclips(subclips)
        final_clip.write_videofile(out_file)
        return True
