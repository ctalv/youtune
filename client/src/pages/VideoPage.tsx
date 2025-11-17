import { useParams } from "react-router";
import { thumbnailArray } from "../test-data";


export default function VideoPage() {
  const iframe = document.getElementById("youtube-iframe");

  function handleIframeLoad() {
    console.log(EventTarget)


    console.log("Iframe content has loaded via addEventListener!");

    // .ytp-chrome-top
    // .ytp-gradient-bottom 
    // .ytp-youtube-button
    // .ytp-pause-overlay-container
  }

  if (iframe) {

    iframe.addEventListener("load", handleIframeLoad)

  }

  const { pk } = useParams();
  const videoItem = thumbnailArray.find((item) => item.pk === Number(pk));

  if (!videoItem) {
    return <div>Video not found {pk}</div>;
  }

  const url = `https://www.youtube.com/embed/${videoItem.videoId}?autoplay=1&modestbranding=1&rel=0`;

  return (
    <>
      <div>
        <div>
          {videoItem.title}
        </div>
        <iframe
          id="youtube-iframe"
          width="700"
          height="350"
          className="video-frame"
          onLoad={handleIframeLoad}
          src={url}>
        </iframe>
        <div>
          {videoItem.description}
        </div>
      </div>
    </>
  );
}

