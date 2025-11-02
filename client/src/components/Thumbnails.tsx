type ThumbnailProps = {
  id: string;
  img: string;
  title: string;
};



type ThumbnailsProps = {
  list: VideoItem[];
};

function Thumbnail({ id, img, title }: ThumbnailProps) {
  return (
    <img  
      className="thumbnail"
      src={img}
      alt={title}
      data-id={id}  
      />
  );
}

export default function Thumbnails({list}: ThumbnailsProps) {
  const thumbnailList = list.map((item) => (
        <Thumbnail
            id={item.videoId}
            img={item.thumbnail}
            title={item.title}
        />
            
    ));

    return <>{thumbnailList}</>
}