import { Link } from 'react-router'
import "../assets/styles/thumbnails.css"

type ThumbnailProps = {
  id: string;
  img: string;
  title: string;
};

type ThumbnailsProps = {
  list: VideoItem[];
};

function Thumbnail({ id, img, title }: ThumbnailProps) {
  const videoLink = `/video/${id}`
  
  return (
    <Link to={videoLink}>
    <img  
      className="thumbnail-img"
      src={img}
      alt={title}
      data-id={id}  
      />
      </Link>
  );
}

export default function Thumbnails({list}: ThumbnailsProps) {
  const thumbnailList = list.map((item) => (
    <div>
        <Thumbnail
            id={String(item.pk)}
            img={item.thumbnail}
            title={item.title}
        />
      </div>
            
    ));

    return (
    <>
      <div>
        {thumbnailList}
      </div>
    </>
  )
}