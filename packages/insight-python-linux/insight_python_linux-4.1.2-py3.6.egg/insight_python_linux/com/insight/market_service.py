


class market_service(object):

    def __init__(self):
        pass

    # ************************************�������ݶ���************************************
    # �����ĵĹ�ƱTick���ݣ�result��ʽΪdict��ʽ
    def on_subscribe_tick(self, result):
        pass


    # �����ĵ�K��ָ��ģ�ͣ�result��ʽΪdict��ʽ
    def on_subscribe_kline(self, result):
        pass


    # ************************************����ط�����************************************
    # ����طŵ�Tick���ݣ�result��ʽΪdict��ʽ
    def on_playback_tick(self, result):
        pass


    # ����طŵ�k�����ݣ�result��ʽΪdict��ʽ
    def on_playback_kline(self, result):
        pass

    # ����طŵ�״̬��status��ʽΪstring��ʽ
    def onPlaybackStatus(self, status):
        pass
        # print(status)

    # ����ط����󷵻ؽ����response��ʽΪstring��ʽ
    def onPlaybackResponse(self, response):
        pass
        # print(response)

    # ����طſ������󷵻ؽ����response��ʽΪstring��ʽ
    def onPlaybackControlResponse(self, response):
        pass
        # print(response)

    # ************************************�����ѯ���󷵻ؽ��************************************
    # �����ѯ�������µ�ָ��֤ȯ�Ļ�����Ϣ�ķ��ؽ����result��ʽΪdict��ʽ
    def on_query_response(self, result):
        pass







    # �����ѯ��ʷ�����е�ָ��֤ȯ�Ļ�����Ϣ query_mdcontant_by_type()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ�������µ�ָ��֤ȯ�Ļ�����Ϣ query_last_mdcontant_by_type()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ��ʷ�����е�ָ��֤ȯ�Ļ�����Ϣ query_mdcontant_by_id()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯ�������µ�ָ��֤ȯ�Ļ�����Ϣ query_last_mdcontant_by_id()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯָ��֤ȯ��ETF�Ļ�����Ϣ query_ETFinfo()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # �����ѯָ��֤ȯ������һ��Tick���� query_last_mdtick()�ķ��ؽ����queryresponse��ʽΪlist[json]
    # def onQueryResponse(self, queryresponse):
    #     pass
        # for resonse in iter(queryresponse):
        #     # response��ʽΪjson��ʽ
        #     print(resonse)

