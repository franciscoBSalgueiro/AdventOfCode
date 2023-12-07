use nom::{
    bytes::complete::tag,
    character::complete::{digit1, space1},
    multi::separated_list1,
    IResult,
};

#[allow(dead_code)]
pub fn int<T>(s: &str) -> IResult<&str, T>
where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    let (input, number) = digit1(s.trim())?;
    Ok((input, number.parse().unwrap()))
}

#[allow(dead_code)]
pub fn list<T>(s: &str) -> IResult<&str, Vec<T>>
where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    separated_list1(space1, int)(s)
}

#[allow(dead_code)]
pub fn matrix<T>(s: &str) -> IResult<&str, Vec<Vec<T>>>
where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    separated_list1(tag("\n"), list)(s)
}
