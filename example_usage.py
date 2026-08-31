from client import NeuralAudioStemSeparationRemasterClient

def main():
    client = NeuralAudioStemSeparationRemasterClient()
    res = client.separate_audio_stems('https://assets.genpark.ai/audio/song_master.wav')
    print('Neural Audio Stem Separator: ' + res['separation_job_id'] + ' (' + str(res['stems_isolated_count']) + ' stems)')
    print('SDR Quality: ' + str(res['signal_to_distortion_ratio_sdr_db']) + ' dB | Bleed Suppression: ' + str(res['artifact_bleed_suppression_pct']) + '%')
    for k, v in res['isolated_stem_urls'].items():
        print('  * Stem [' + k + ']: ' + v)

if __name__ == '__main__':
    main()
