import connexion
import six

from TimeSeriesIoT import util


def mean_sensor_id_get(sensor_id, start_date, end_date):  # noqa: E501
    """Renvoie la moyenne d&#39;un capteur entre deux dates

    Description optionnelle. # noqa: E501

    :param sensor_id: L&#39;identifiant du capteur où récupérer les données.
    :type sensor_id: str
    :param start_date: Integer/timestamp de la date de début.
    :type start_date: int
    :param end_date: Integer/timestamp de la date de fin.
    :type end_date: int

    :rtype: List[int]
    """
    return 'Sensor : ' + sensor_id + ' [start:end] : [' + str(start_date) + ':' + str(end_date) + ']'
    
