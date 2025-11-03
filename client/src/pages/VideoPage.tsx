import { useParams } from "react-router";
import { thumbnailArray } from "../test-data";

export default function VideoPage() {
  const { pk } = useParams();
  const videoItem = thumbnailArray.find((item) => item.pk === Number(pk));

  if (!videoItem) {
    return <div>Video not found {pk}</div>;
  }

  const url = `https://www.youtube.com/embed/${videoItem.videoId}`;

  return (
    <>
    <div>
        <div>
            {videoItem.title}
        </div>
        <iframe width="420" height="315"
            src={url}>
        </iframe> 
        <div>
            {videoItem.description}
        </div>
    </div>
    </>
  );
}
 
