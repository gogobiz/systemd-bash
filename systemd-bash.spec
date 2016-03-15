#% define beta_tag rc2
%define patchleveltag .46
%define baseversion 4.2
%define oname bash 
%bcond_without tests

Version: %{baseversion}%{patchleveltag}
Name: systemd-bash
Summary: The GNU Bourne Again shell
Release: 19%{?dist}
Group: System Environment/Shells
License: GPLv3+
Url: http://www.gnu.org/software/bash
Source0: ftp://ftp.gnu.org/gnu/bash/bash-%{baseversion}.tar.gz

Requires: systemd-libs pcre glibc elfutils-libelf bzip2-libs xz-libs libselinux libcap ncurses-libs  libattr
BuildRequires: texinfo bison
BuildRequires: ncurses-devel
BuildRequires: autoconf, gettext
Conflicts: filesystem < 3
Provides: /bin/sh
Provides: /bin/bash

%description
The GNU Bourne Again shell (Bash) is a shell or command language
interpreter that is compatible with the Bourne shell (sh). Bash
incorporates useful features from the Korn shell (ksh) and the C shell
(csh). Most sh scripts can be run by bash without modification.

%prep
#%setup -q -a 2
%setup -q -n %{oname}-%{baseversion}

echo %{version} > _distribution
echo %{release} > _patchlevel

%build
autoconf
%configure --with-bash-malloc=no --with-afs 

# Recycles pids is neccessary. When bash's last fork's pid was X
# and new fork's pid is also X, bash has to wait for this same pid.
# Without Recycles pids bash will not wait.
make "CPPFLAGS=-D_GNU_SOURCE -DRECYCLES_PIDS -DDEFAULT_PATH_VALUE='\"/usr/local/bin:/usr/bin\"' `getconf LFS_CFLAGS`"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
cp bash $RPM_BUILD_ROOT/bin/systemd-bash

%post
rm -f /bin/bash
if [ -f /bin/bash ]; then
 mv /bin/bash /bin/bash.orig
fi
ln -s /bin/systemd-bash /bin/bash

%postun
rm -f /bin/bash
if [ -f /bin/bash.orig ]; then
 mv /bin/bash.orig /bin/bash
fi

%if %{with tests}
%check
make check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/bin/systemd-bash

