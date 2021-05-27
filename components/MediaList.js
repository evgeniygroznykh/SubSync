import React, { useState, useEffect } from 'react'
import appConfig from './react-app-config'
import videoimg from './img/video.jpg'
import subtitleimg from './img/subtitle.jpg'
 

export default function MediaList (props) {
    const [clips, setClips] = useState([])
    const [subtitles, setSubtitles] = useState([])
    const [error, setError] = useState("")

    const selected_channel = props.selected_channel ? props.selected_channel : ""

    useEffect(() => {
        if (selected_channel) {
            const apiBaseUrl = appConfig.api_base_url

            fetch(`${apiBaseUrl}/get_clips/${selected_channel}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setClips(result)
                },
                (error) => {
                    setError(error)
                }
            )

            fetch(`${apiBaseUrl}/get_subtitles/${selected_channel}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setSubtitles(result)
                },
                (error) => {
                    setError(error)
                }
            )
        }
    }, [selected_channel])

    if (error) {
        return (
            <div>
                {error.message}
            </div>
        )
    }
    else {
        return (
            <div id="media-content">
                <div id='clip-list-container'>
                    <table id="clip-list">
                        <thead>
                            <tr>
                                <th>Clips:</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                clips.map((clip, index) => {
                                    return (
                                        <div>
                                            <tr key={index}>
                                                <td><span><img className="icon" src={videoimg} alt=""></img>{clip}</span></td>
                                            </tr>
                                        </div>
                                        )
                                    }
                                )
                            }
                        </tbody>
                    </table>
                </div>
                <div id='subtitle-list-container'>
                <table id="subtitle-list">
                    <thead>
                        <tr>
                            <th>Subtitles:</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            subtitles.map((subtitle, index) => {
                                return (
                                    <div>
                                        <tr key={index}>
                                            <td><span><img className="icon" src={subtitleimg} alt=""></img>{subtitle}</span></td>
                                        </tr>
                                    </div>
                                    )
                                }
                            )
                        }
                    </tbody>
                    </table>
                </div>
            </div>
        )
    }
}