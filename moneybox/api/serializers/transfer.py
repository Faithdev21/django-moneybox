from rest_framework.serializers import ModelSerializer

from wallet.models.transfer import Transfer


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
