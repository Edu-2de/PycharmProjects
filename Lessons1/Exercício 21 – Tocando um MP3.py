#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import data
import soundfile as sf

samplerate = sf.read("C:\Users\Eduardo Paim\PycharmProjects\Curso-em-video\.aulas\Audioslave.wav")
sf.play(data, samplerate)
