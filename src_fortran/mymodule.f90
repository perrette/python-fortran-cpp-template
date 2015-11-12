module operators
  implicit none
  ! Various basic operators to illustrate ways
  ! of passing arrays to and getting them back
  ! from fortran.

contains

  ! Use subroutine, and implied size dynamic arrays
  subroutine array_add(x1, x2, res)
    double precision, intent(in) :: x1(:)
    double precision, intent(in) :: x2(:)
    double precision, intent(out) :: res(size(x1))

    if (size(x1) /= size(x2)) then 
      write(*,*) "Wrong input array size, will crash"
    endif

    res = x1 + x2
  end subroutine

  ! Indicate size explicitly (improved clarity ?)
  subroutine array_div(x1, x2, n, res)
    double precision, intent(in) :: x1(n)
    double precision, intent(in) :: x2(n)
    integer, intent(in) :: n
    double precision, intent(out) :: res(n)

    if (size(x1) /= size(x2)) then 
      write(*,*) "Wrong input array size, will crash"
    endif

    res = x1 / x2
  end subroutine

  ! Function (I like that in pure fortran - kind of clearer)
  ! But f2py wraps everything to functions anyway based on 
  ! intent, so this does not make any difference.
  function array_mult(x1, x2) result(res)
    double precision, intent(in) :: x1(:)
    double precision, intent(in) :: x2(:)
    double precision :: res(size(x1))

    if (size(x1) /= size(x2)) then 
      write(*,*) "Wrong input array size, will crash"
    endif

    res = x1 * x2
  end function

end module
