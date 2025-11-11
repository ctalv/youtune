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
    <Link to={videoLink} title={title}>
      <img
        className="thumbnail-img"
        src={img}
        alt={title}
        data-id={id}

      />
      <h3 className='thumbnail-title'>{title}</h3>
    </Link>
  );
}

export default function Thumbnails({ list }: ThumbnailsProps) {
  const thumbnailList = list.map((item) => (
    <div className='thumbnail-container'>
      <Thumbnail
        id={String(item.pk)}
        img={item.thumbnail}
        title={item.title}
      />
    </div>

  ));

  return (
    <>
      <div className='thubnail-list'>
        {thumbnailList}
      </div>
    </>
  )
}