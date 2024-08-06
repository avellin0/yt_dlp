Conversa com chatGPT:

--Eu:

 O yt_dlp so precisa chamar uma função `YoutubeDL` que por sua vez tem  apenas um parametro, que deve ser um objeto contendo o formato , o nome ao qual vai ser criado uma instância (output) e algumas opções pessoais como "noplaylist" que indica se quer ou não baixar uma playlist inteira. depois deve fazer uma instância dessa função com os parametros passado e chamar uma outra função chamada "download" que deve passar a url do video

 ex: 

``
 config_do_video = {
         'format': 'bestvideo[ext=mp4]/best'
         'outtmpl': 'video.mp4',
         'noplaylist': True
       }

 with yt_dlp.YoutubeDL(config_do_video) as ydl:
   print('Baixando o audio...)
    ydl.download([Youtube_url])
``

-- ChatGPT:

Exatamente, você captou bem a ideia!

Vamos revisar os pontos principais:

Instanciação de YoutubeDL:

A classe YoutubeDL é inicializada com um dicionário de opções (ydl_opts) que define o formato de download, o nome do arquivo de saída, e outras opções (como noplaylist).
Método download:

Após criar a instância de YoutubeDL, você chama o método download e passa a URL do vídeo que deseja baixar.
Aqui está uma visão geral simplificada:


import yt_dlp

ydl_opts = {
    'format': 'bestvideo[ext=mp4]/best',  # Formato do vídeo
    'outtmpl': 'video.mp4',  # Nome do arquivo de saída
    'noplaylist': True  # Não baixar a playlist inteira
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  
ydl.download(['https://www.youtube.com/watch?v=VW5ujnrRDTg'])
yt_dlp.YoutubeDL(ydl_opts): Cria uma instância da classe YoutubeDL com as opções definidas.
ydl.download([youtube_url]): Faz o download do vídeo a partir da URL fornecida.
Se precisar de mais alguma coisa ou tiver outras dúvidas, é só falar!




# OBS:

'format': `bestaudio[ext=mp3]/best`

`bestaudio` = Acho que não precisa de muita explicação né (melhor audio)
`[ext=mp3]` = É uma forma de filtro , dizendo que quer o tipo mp3 
`/best` = Significa que se não achar o tipo que você deseja (mp3) vai pegar o melhor


# NOTAS IMPORTANTES

## 1°
 Se você rodar esses códigos como `audio.py` ou `teste.py` eles vão criar dois arquivos , um sendo `.mp4` e o outro `.mp3`
 separadamente , para você unir esses dois arquivos e tranforma em um video com audio você deve usar um comando no terminal:

`ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -b:a 192k -filter_complex "[1]adelay=1000|1000[a]" -map 0:v -map "[a]" video.mp4`

troque "video" e "audio" pelo valor de  `'outtmpl': 'video.mp4'`
                                           esse =>     ☝
                                           