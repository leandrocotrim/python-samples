# coding: utf-8
import io
import sys
import urllib.request as request

class Copa:
    '''
    Class copa
    Cap. 4
    '''   
    def main():
        print('Executo pela linha de comando.')
        response = request.urlopen(sys.argv[1])
        out_file = io.FileIO('saida.zip', mode='w')

        content_length = response.getheader('Content-Length')
        if content_length:
            length = int(content_length)
            download_length(response, out_file, length)
        else:
            download(response, out_file)
        
        response.close()
        out_file.close()
        print('Finished')
        
    if __name__ == '__main__':
        main()

    BUFF_SIZE = 1024

    def __init__(self):
        '''
        construtor padrão
        '''
    
    def download_length(response, output, length):
        '''
        download com length vindo do servidor
        '''
        times = length // BUFF_SIZE
        if length % BUFF_SIZE > 0:
            time += 1
        
        for time in range(times):
            output.write(response.read(BUFF_SIZE))
            print('Download %d' % (((time * BUFF_SIZE) / length) * 100))

    def download(response, output):
        '''
        download sem length vindo do servidor
        '''
        total_downloaded = 0
        while True:
            data = response.read(BUFF_SIZE)
            total_downloaded += len(data)
            if not data:
                break;
            output.write(data)
            print('Downloaded {bytes}'.format(bytes=total_downloaded))


# print(Copa.__doc__)
# print(Copa.__init__.__doc__)
# print(Copa.download_length.__doc__)