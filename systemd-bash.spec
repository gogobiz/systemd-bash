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

# For now there isn't any doc
#Source2: ftp://ftp.gnu.org/gnu/bash/bash-doc-%{version}.tar.gz

Source1: dot-bashrc
Source2: dot-bash_profile
Source3: dot-bash_logout

# Official upstream patches
Patch001: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-001
Patch002: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-002
Patch003: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-003
Patch004: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-004
Patch005: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-005
Patch006: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-006
Patch007: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-007
Patch008: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-008
Patch009: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-009
Patch010: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-010
Patch011: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-011
Patch012: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-012
Patch013: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-013
Patch014: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-014
Patch015: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-015
Patch016: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-016
Patch017: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-017
Patch018: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-018
Patch019: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-019
Patch020: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-020
Patch021: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-021
Patch022: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-022
Patch023: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-023
Patch024: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-024
Patch025: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-025
Patch026: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-026
Patch027: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-027
Patch028: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-028
Patch029: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-029
Patch030: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-030
Patch031: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-031
Patch032: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-032
Patch033: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-033
Patch034: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-034
Patch035: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-035
Patch036: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-036
Patch037: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-037
Patch038: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-038
Patch039: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-039
Patch040: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-040
Patch041: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-041
Patch042: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-042
Patch043: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-043
Patch044: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-044
Patch045: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-045
Patch046: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-046
#1175647 - shellshock related parser bugs
Patch052: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-052
Patch053: ftp://ftp.gnu.org/pub/gnu/bash/bash-4.2-patches/bash42-053

# Other patches
Patch101: bash-2.02-security.patch
Patch102: bash-2.03-paths.patch
Patch103: bash-2.03-profile.patch
Patch104: bash-2.05a-interpreter.patch
Patch105: bash-2.05b-debuginfo.patch
Patch106: bash-2.05b-manso.patch
Patch107: bash-2.05b-pgrp_sync.patch
Patch108: bash-2.05b-readline-oom.patch
Patch109: bash-2.05b-xcc.patch
Patch110: bash-3.2-audit.patch
Patch111: bash-3.2-ssh_source_bash.patch
Patch112: bash-bashbug.patch
Patch113: bash-infotags.patch
Patch114: bash-requires.patch
Patch115: bash-setlocale.patch
Patch116: bash-tty-tests.patch

# 484809, check if interp section is NOBITS
Patch117: bash-4.0-nobits.patch

# Do the same CFLAGS in generated Makefile in examples
Patch118: bash-4.1-examples.patch

# Builtins like echo and printf won't report errors
# when output does not succeed due to EPIPE
Patch119: bash-4.1-broken_pipe.patch

# Enable system-wide .bash_logout for login shells
Patch120: bash-4.2-rc2-logout.patch

# Static analyzis shows some issues in bash-2.05a-interpreter.patch
Patch121: bash-4.2-coverity.patch

# Don't call malloc in signal handler
Patch122: bash-4.1-defer-sigchld-trap.patch

# 799958, updated info about trap
Patch123: bash-4.2-manpage_trap.patch

# 695656, block the signal and unblock it after the new handler is installed
Patch124: bash-4.2-signal.patch

# https://www.securecoding.cert.org/confluence/display/seccode/INT32-C.+Ensure+that+operations+on+signed+integers+do+not+result+in+overflow
Patch125: bash-4.2-size_type.patch

# 903833, Fix missing close(), fixes fd leaks
Patch126: bash-4.2-missing_closes.patch
Patch127: bash-4.1-trap.patch

# 1112709 - mention ulimit -c and -f POSIX block size
Patch128: bash-4.2-man-ulimit.patch

# 1116301 - inhibit brace expansion in some cases
Patch129: bash-4.2-brace-expand.patch

# 1102813 - fix bash visual mode
Patch130: bash-4.2-noecho.patch

# 1126370 - provide a better description for some bash builtins
Patch131: bash-4.2-manpage.patch

# 1126396 - prevent bash from hanging with certain history settings
Patch132: bash-4.2-history-hang.patch

# 1126401 - properly document extglob behaviour
Patch133: bash-4.2-extglob-man.patch

# 1141648 - properly document extglob behaviour
Patch134: bash-4.2-env-inject.patch

# 1146324 - cve-2014-7169

Patch135: bash-4.2-cve-2014-7169-0.patch
Patch136: bash-4.2-cve-2014-7169-1.patch
Patch137: bash-4.2-cve-2014-7169-2.patch

#1172214 - Bash leaks memory when doing a pattern-substitution
Patch138: bash-4.2-double-alloc.patch

#1196566 - IFS incorrectly splitting herestrings
Patch139: bash-4.2-ifs-in-temp-env.patch

#1165793
Patch140: bash-4.2-check-debugger.patch

#1212775
Patch141: bash-4.2-case-in-command-subst.patch

#1237213 - export when fnname contains hyphens
Patch142: bash-4.2-enable-hyphened-fn-export.patch

Patch900: bash-alarm.patch

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

%package doc
Summary: Documentation files for %{oname}
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{oname}.

%define pkgdocdir %{_datadir}/doc/%{oname}-%{version}

%prep
#%setup -q -a 2
%setup -q -n %{oname}-%{baseversion}

# Official upstream patches
%patch001 -p0 -b .001
%patch002 -p0 -b .002
%patch003 -p0 -b .003
%patch004 -p0 -b .004
%patch005 -p0 -b .005
%patch006 -p0 -b .006
%patch007 -p0 -b .007
%patch008 -p0 -b .008
%patch009 -p0 -b .009
%patch010 -p0 -b .010
%patch011 -p0 -b .011
%patch012 -p0 -b .012
%patch013 -p0 -b .013
%patch014 -p0 -b .014
%patch015 -p0 -b .015
%patch016 -p0 -b .016
%patch017 -p0 -b .017
%patch018 -p0 -b .018
%patch019 -p0 -b .019
%patch020 -p0 -b .020
%patch021 -p0 -b .021
%patch022 -p0 -b .022
%patch023 -p0 -b .023
%patch024 -p0 -b .024
%patch025 -p0 -b .025
%patch026 -p0 -b .026
%patch027 -p0 -b .027
%patch028 -p0 -b .028
%patch029 -p0 -b .029
%patch030 -p0 -b .030
%patch031 -p0 -b .031
%patch032 -p0 -b .032
%patch033 -p0 -b .033
%patch034 -p0 -b .034
%patch035 -p0 -b .035
%patch036 -p0 -b .036
%patch037 -p0 -b .037
%patch038 -p0 -b .038
%patch039 -p0 -b .039
%patch040 -p0 -b .040
%patch041 -p0 -b .041
%patch042 -p0 -b .042
%patch043 -p0 -b .043
%patch044 -p0 -b .044
%patch045 -p0 -b .045
%patch046 -p0 -b .046

# Other patches
%patch101 -p1 -b .security
%patch102 -p1 -b .paths
%patch103 -p1 -b .profile
%patch104 -p1 -b .interpreter
%patch105 -p1 -b .debuginfo
%patch106 -p1 -b .manso
%patch107 -p1 -b .pgrp_sync
%patch108 -p1 -b .readline_oom
%patch109 -p1 -b .xcc
%patch110 -p1 -b .audit
%patch111 -p1 -b .ssh_source_bash
%patch112 -p1 -b .bashbug
%patch113 -p1 -b .infotags
%patch114 -p1 -b .requires
%patch115 -p1 -b .setlocale
%patch116 -p1 -b .tty_tests
%patch117 -p1 -b .nobits
%patch118 -p1 -b .examples
%patch119 -p1 -b .broken_pipe
%patch120 -p1 -b .logout
%patch121 -p1 -b .coverity
%patch122 -p1 -b .defer_sigchld_trap
%patch123 -p1
%patch124 -p1 -b .signal
%patch125 -p1 -b .size_type
%patch126 -p1 -b .missing_closes
%patch127 -p1 -b .trap
%patch128 -p1 -b .ulimit
%patch129 -p1 -b .expand
%patch130 -p1 -b .noecho
%patch131 -p1 -b .manpage
%patch132 -p1 -b .hang
%patch133 -p1 -b .man
%patch134 -p0 -b .inject
%patch135 -p0 -b .7169-0
%patch136 -p0 -b .7169-1
%patch137 -p0 -b .7169-2
%patch052 -p0 -b .052
%patch053 -p0 -b .053
%patch138 -p1 -b .double-alloc
%patch139 -p1 -b .temp-env
%patch140 -p1 -b .check-debugger
%patch141 -p1 -b .command-subst
%patch142 -p0 -b .export
%patch900 -p1 -b .alarm

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
mkdir -p $RPM_BUILD_ROOT/etc/jaguar/bin
cp bash $RPM_BUILD_ROOT/etc/jaguar/bin

%post
rm -f /bin/bash
if [ -f /bin/bash ]; then
 mv /bin/bash /bin/bash.orig
fi
ln -s /etc/jaguar/bin/bash /bin/bash

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
/etc/jaguar/bin/bash

