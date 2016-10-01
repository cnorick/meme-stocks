CREATE TABLE Memes
(
memeID int not null PRIMARY KEY identity,
memeName nvarchar(max),
memePicture varbinary(max)
);

CREATE TABLE memeStats
(
memeStatsID int not null PRIMARY KEY identity,
memeID int,
timestamp datetime2,
score int,
foreign key(memeID) references memes(memeID)
);



CREATE PROCEDURE getMemes
AS
BEGIN

select *
from memes

END