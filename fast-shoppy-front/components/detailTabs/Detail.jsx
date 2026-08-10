import { ImageList } from '@/components/commons/ImageList.jsx';

export default function Detail({ imgList, pid, detailInfo }) {
  if (!detailInfo) return <div>상세 정보가 없습니다.</div>;

  return (
    <div>
      <DetailImages imgList={imgList} />
      <DetailInfo info={detailInfo} />
    </div>
  );
}

export function DetailImages({ imgList }) {
  return (
    <div className="detail-images">
      <div style={{ padding: '20px' }}></div>
      <img src="/images/holidays_notice.jpg" alt="notice" />
      <ImageList imgList={imgList} className="detail-images-list" />
    </div>
  );
}

export function DetailInfo({ info }) {
  
  return (
    <div className="detail-info">
      <h4 className="detail-info-title-top">
        {info?.title_en} / {info?.title_ko}
        {info?.list && info.list.map((item, idx) => (
          <div key={idx}>
            <h5 className="detail-info-title">[{item.title}]</h5>
            {item.title === 'SIZE' || item.title === 'RIDER INFO' ? (
              <ul className="nolist">
                <li>{item.type}</li>
                {item.title === 'RIDER INFO' && <><li>{item.height}</li><li>{item.size}</li></>}
                {item.title === 'SIZE' && (
                  <>
                    <li>전장: {item.totalLength}</li>
                    <li>휠 사이즈: {item.shoulderWidth}</li>
                    <li>탑튜브 길이: {item.chestWidth}</li>
                    <li>시트튜브 길이: {item.sleeveLength}</li>
                  </>
                )}
              </ul>
            ) : (
              <ul className="list nolist">
                {item.title === 'FRAME' && <><li>Color: {item.color}</li><li>{item.material}</li></>}
                {item.description?.map((desc, i) => <li key={i}>{desc}</li>)}
              </ul>
            )}
          </div>
        ))}
      </h4>
    </div>
  );
}
